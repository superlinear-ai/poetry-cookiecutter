"""Base class for SQL database CRUD based on: https://github.com/tiangolo/full-stack-fastapi-postgresql."""
from __future__ import annotations

from typing import Any, Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import or_
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session, selectinload

from orm.models.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Base class for SQL database CRUD.

    ModelType: A SQLAlchemy model class.
    CreateSchemaType: a pydantic schema with all data required to create a db entry.
    UpdateSchemaType: a pydantic schema with all data required to update a db entry.
    """

    # Options to be used to control how relationships are loaded when querying the database with the recursive option.
    # Overwrite in derived classes to control loading of specific relationships.
    recursive_options = (selectinload("*"),)

    def __init__(self, model: Type[ModelType]):
        """CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        Parameters
        ----------
        model : Type[ModelType]
             A SQLAlchemy model class
        """
        self.model = model

    def encode(self, obj_in: CreateSchemaType) -> dict[str, Any]:
        """Map from a CreateSchemaType object to a dict containing arguments for a ModelType object.

        Session is added as a parameter to keep function signature consistent with subclasses which requite a session
        for encoding.
        """
        r: dict[str, Any] = jsonable_encoder(obj_in)
        return r

    def encode_update(
        self, obj_in: UpdateSchemaType | dict[str, Any]
    ) -> dict[str, Any]:
        """Map from a UpdateSchemaType object to a dict containing arguments for a ModelType object.

        Contains extra logic to ensure unset parameters don't overwrite values with "None"s.

        Session is added as a parameter to keep function signature consistent with subclasses which requite a session
        for encoding.
        """
        return (
            obj_in
            if isinstance(obj_in, dict)
            else obj_in.dict(exclude_unset=True, exclude_none=True)
        )

    def get(
        self,
        session: Session,
        id: Any,
        recursive: bool = False,
        owner: str | None = None,
        is_admin: bool = False,
    ) -> ModelType | None:
        """Get a single object from the database based on its id.

        Parameters
        ----------
        session
            Database session.
        id
            Desired object id.
        recursive
            Whether to try to load relationships eagerly.

        Returns
        -------
        Optional[ModelType]
            Requested object or None if it id is not found.
        """
        base_query = (
            session.query(self.model)
            .filter(
                or_(self.model.owner == owner, self.model.public)
                if owner and not is_admin
                else True
            )
            .filter(self.model.id == id)
        )
        if recursive:
            base_query = base_query.options(*self.recursive_options)

        r: ModelType | None = base_query.first()
        return r

    def get_multi(
        self,
        session: Session,
        sort_by: Any = "id",
        skip: int = 0,
        limit: int = 100,
        recursive: bool = False,
        asc: bool = True,
        owner: str | None = None,
        ids: list[int] | None = None,
        is_admin: bool = False,
    ) -> list[ModelType]:
        """Get all objects from a database table.

        Parameters
        ----------
        session
            Database session.
        sort_by
            The column to sort by.
        skip
            Number of objects (offset) to skip.
        limit
            Maximum number of objects to return.
        recursive
            Whether to try to load relationships eagerly.
        asc
            Whether to sort in ascending order.
        owner
            The owner of the objects to return.
        ids
            A list of ids of the objects to return.
        is_admin
            Whether the owner is an admin.

        Returns
        -------
        List[ModelType]
            Requested objects.
        """
        if not hasattr(self.model, sort_by):
            raise ValueError(f"The sorting criterion {sort_by} is not a column in {self.model}.")

        base_query = (
            session.query(self.model)
            .filter(
                or_(self.model.owner == owner, self.model.public)
                if owner and not is_admin
                else True
            )
            .filter(self.model.id.in_(ids) if ids else True)
            .order_by(
                getattr(self.model, sort_by).asc() if asc else getattr(self.model, sort_by).desc()
            )
            .offset(skip)
            .limit(limit)
        )

        if recursive:
            base_query = base_query.options(*self.recursive_options)

        r: list[ModelType] = base_query.all()

        return r

    def create(self, session: Session, obj_in: CreateSchemaType) -> ModelType:
        """Create a new database entry.

        Parameters
        ----------
        session
            Database session.
        obj_in
            Object create schema.

        Returns
        -------
        ModelType
            Created object.
        """
        obj_in_data = self.encode(obj_in, session=session)
        db_obj: ModelType = self.model(**obj_in_data)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def create_multi(self, session: Session, objs_in: list[CreateSchemaType]) -> list[ModelType]:
        """Create multiple objects at once.

        Parameters
        ----------
        session
            Database session.
        obj_in
            List of object create schemas.

        Returns
        -------
        List[ModelType]
            Created objects.
        """
        db_objs: list[ModelType] = [
            self.model(**self.encode(obj_in, session=session)) for obj_in in objs_in
        ]
        session.add_all(db_objs)
        session.commit()
        for db_obj in db_objs:
            session.refresh(db_obj)
        return db_objs

    def update(
        self, session: Session, *, id: Any, obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        """Update an existing object.

        Parameters
        ----------
        session
            Database session.
        id
            ID of object to update.
        obj_in
            New values for object attributes.

        Returns
        -------
        ModelType
            Updated object

        Raises
        ------
        NoResultFound
            Raised if object with given id does not exist.
        """
        db_obj: ModelType | None = self.get(session, id)
        if db_obj is None:
            raise NoResultFound()

        update_data = self.encode_update(obj_in, session)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def remove(self, session: Session, *, id: int) -> ModelType | None:
        """Remove an object from the database.

        Parameters
        ----------
        session
            Database session.
        id
            ID of object to remove.

        Returns
        -------
        ModelType
            Removed object.
        """
        db_obj: ModelType | None = session.query(self.model).get(id)
        if db_obj is None:
            raise NoResultFound()
        session.delete(db_obj)
        session.commit()
        return db_obj
