

from invoke import task

from fanfic.database import engine
from fanfic.models import Base


@task
def init_db(ctx):

    """
    Create database tables.
    """

    Base.metadata.create_all(engine)


@task
def reset_db(ctx):

    """
    Drop and recreate database tables.
    """

    Base.metadata.drop_all(engine)

    init_db(ctx)
