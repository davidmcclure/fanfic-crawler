

import pytest

from fanfic.singletons import config as _config, session
from fanfic.models import Base


@pytest.fixture(scope='session', autouse=True)
def init_testing_db():

    """
    Drop and recreate the tables.
    """

    engine = _config.build_sqla_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture
def db():

    """
    Wrap tests inside a transaction.
    """

    session.begin_nested()

    yield

    session.remove()


@pytest.yield_fixture(scope='module')
def db_module():
    yield from db()
