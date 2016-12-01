

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL


# TODO: Config-ify.


url = URL(**dict(
    drivername='postgres',
    database='fanfic',
))

engine = create_engine(url)

# Fix transaction bugs in pysqlite.

@event.listens_for(engine, 'connect')
def connect(conn, record):
    conn.isolation_level = None

@event.listens_for(engine, 'begin')
def begin(conn):
    conn.execute('BEGIN')


factory = sessionmaker(engine)

session = scoped_session(factory)
