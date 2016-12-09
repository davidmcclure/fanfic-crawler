

import pytest

from fanfic.database import session
from fanfic.models import MetadataHTML, Metadata
from fanfic.utils import read_yaml


cases = read_yaml(__file__, 'fixtures.yml')


@pytest.fixture(scope='module', autouse=True)
def ingest(db_module):

    """
    Write HTML fixtures into the database.
    """

    for book_id, case in cases.items():
        row = MetadataHTML(book_id=book_id, html=case['html'])
        session.add(row)

    MetadataHTML.ingest()


@pytest.mark.parametrize('book_id,case', cases.items())
def test_ingest(book_id, case):

    row = Metadata.query.filter_by(book_id=book_id).one()

    for key, val in case['fields'].items():
        assert getattr(row, key) == val
