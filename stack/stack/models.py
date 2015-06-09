from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """ Performs database connections using database settings from settings.py
        Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_reals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Reals(DeclarativeBase):
    """SQLAlchemy Reals Model"""
    __tablename__ = 'reals'

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
