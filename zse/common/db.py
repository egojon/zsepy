from zse.common import logging
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

log = logging.getLogger()

DB_USER = os.environ.get('ZSE_DB_USER', 'root')
DB_PASSWORD = os.environ.get('ZSE_DB_PASSWORD', '1337')
DB_HOST = os.environ.get('ZSE_DB_HOST', 'localhost')
DB_DATABASE = os.environ.get('ZSE_DB_DATABASE', 'zsepy')

CONNECTION_STRING = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(CONNECTION_STRING)

create_session = sessionmaker(bind=engine)

session = create_session()

metadata = MetaData(bind=engine)

Base = declarative_base(bind=engine, metadata=metadata)


def start_session():
    global session
    session = create_session()


def end_session():
    global session
    session.commit()
    session.close()
    session = None


def build(data: dict, obj_type):
    obj = obj_type()
    obj_type_fields = [x for x in obj_type.__dict__ if not x.startswith('_')]
    for k, v in data.items():
        if k in obj_type_fields:
            setattr(obj, k, v)
    return obj
