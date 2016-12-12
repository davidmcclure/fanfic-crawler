

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

    (244872071, dict(
        review_id=244872071,
        book_id=11403360,
        user_id=5354915,
        username='Mawenn35',
        chapter_number=14,
        review="Please update soon ! I want to see how Minerva will react !",
        published=dt.fromtimestamp(1481500327),
    )),

    # Guest user with default "Guest" name.
    (244833729, dict(
        review_id=244833729,
        book_id=11403360,
        user_id=None,
        username='Guest',
        chapter_number=13,
        review="I love minerva mcgonagall awesome i can't wait more",
        published=dt.fromtimestamp(1481408736),
    )),

    # Guest user with custom name.
    (244481472, dict(
        review_id=244481472,
        book_id=11403360,
        user_id=None,
        username='dsky',
        chapter_number=13,
        review="This is great. Your OC\"s are very interesting, and I like the trips through the mablomi as a way for Harry and Hermione to figure things out. I'm a sucker for MM/AD too. It will be awesome if Albus is alive. I hope he comes back in time to help them fight whoever it was that gave Umbridge the knife. I'm looking forward to more!",  # noqa: E501
        published=dt.fromtimestamp(1480485582),
    )),

])
def test_ingest(review_id, fields):

    row = Review.query.filter_by(review_id=review_id).one()

    for key, val in fields.items():
        assert getattr(row, key) == val
