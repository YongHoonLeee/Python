import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import ext
from sqlalchemy import Column
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite://:memory:')
Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'Persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, PRIMARY_KEY = True , AUTOINCREMENT = True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)




