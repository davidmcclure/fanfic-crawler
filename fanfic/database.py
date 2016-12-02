

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL


# TODO: Config-ify.

url = URL(**dict(
    drivername='sqlite',
    database='fanfic.db',
))


# Build engine.

engine = create_engine(url)

@event.listens_for(engine, 'connect')
def connect(conn, record):
    conn.isolation_level = None

@event.listens_for(engine, 'begin')
def begin(conn):
    conn.execute('BEGIN')


factory = sessionmaker(engine)

session = scoped_session(factory)
