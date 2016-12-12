

import pytest

from datetime import datetime as dt

from fanfic.models import ReviewHTML, Review
from fanfic.database import session
from fanfic.utils import flatten_dict

from test.utils import read_yaml


cases = read_yaml(__file__, 'ingest.yml')


@pytest.fixture(scope='module', autouse=True)
def ingest(db_module):

    """
    Write HTML fixtures into the database.
    """

    for (book_id, _), html in flatten_dict(cases):
        row = ReviewHTML(book_id=book_id, html=html)
        session.add(row)

    ReviewHTML.ingest()


@pytest.mark.parametrize('review_id,fields', [

    (244875348, dict(
        review_id=244875348,
        book_id=11403360,
        user_id=8550699,
        username='Ramona125',
        chapter_number=1,
        review="I love your story! Great writing! Please update soon. I would love to find out how Minerva's going to react and how the story's going to continue.",  # noqa: E501
        published=dt.fromtimestamp(1481506897),
    )),

])
def test_ingest(review_id, fields):

    row = Review.query.filter_by(review_id=review_id).one()

    for key, val in fields.items():
        assert getattr(row, key) == val
