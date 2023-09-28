"""SQLAlchemy model definitions."""

from __future__ import annotations


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta


Base: DeclarativeMeta = declarative_base()