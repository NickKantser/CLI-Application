from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import mapper, relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://elsjbyqx:thpxz1QRoIbx34LqqsgLsAG3kdxCcfGg@lallah.db.elephantsql.com:5432/elsjbyqx')
Base = declarative_base(engine)

metadata = Base.metadata
Session = sessionmaker(bind=engine)
session = Session()
