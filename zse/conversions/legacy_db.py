from zse.common import logging
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

log = logging.getLogger()

DB_USER = os.environ.get('LEGACY_DB_USER', 'root')
DB_PASSWORD = os.environ.get('LEGACY_DB_PASSWORD', '1337')
DB_HOST = os.environ.get('LEGACY_DB_HOST', 'localhost')
DB_DATABASE = os.environ.get('LEGACY_DB_DATABASE', 'zseweb_new')

CONNECTION_STRING = 'mysql+pymysql://%s:%s@%s/%s' % (DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE)

engine = create_engine(CONNECTION_STRING)

create_session = sessionmaker(bind=engine)

session = create_session()

metadata = MetaData(bind=engine)
