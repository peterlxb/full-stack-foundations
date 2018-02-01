import sys
from sqlalchemy import Column, ForeignKey,Integer,String, create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


#engine = create_engine('sqlite://root:password@localhost:3306/test')

DBSession = sessionmaker(bind=engine)
