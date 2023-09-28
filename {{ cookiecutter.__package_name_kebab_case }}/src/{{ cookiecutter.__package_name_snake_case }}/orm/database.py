"""Instantiate the necessary SQLAlchemy singleton objects for communicating with the database."""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from orm.models.models import Base

# Modify the following variables to change the database connection to cloud services or other databases.
DB_CONN = "sqlite:///./db.sqlite3"
DB_CONNECTION_ARGS = {"check_same_thread": False}

# Singleton engine object
engine = create_engine(DB_CONN, future=True, connect_args=DB_CONNECTION_ARGS)

# We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
SessionLocal = sessionmaker(bind=engine)


def initialize_db() -> None:
    """Recreate the database based on structure defined by models."""
    Base.metadata.create_all(engine)


def reset_db() -> None:
    """Recreate the database based on structure defined by models."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get a DB Session.

    Yields
    ------
        DB session object.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


if __name__ == "__main__":
    reset_db()
