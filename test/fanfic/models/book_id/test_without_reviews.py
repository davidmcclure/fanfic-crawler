

import pytest

from fanfic.models import BookId

from test.factories import BookIdFactory, ReviewHTMLFactory


pytestmark = pytest.mark.usefixtures('db')


def test_without_chapters():

    BookIdFactory(book_id=1)
    BookIdFactory(book_id=2)
    BookIdFactory(book_id=3)
    BookIdFactory(book_id=4)

    ReviewHTMLFactory(book_id=1)
    ReviewHTMLFactory(book_id=1)

    ReviewHTMLFactory(book_id=2)
    ReviewHTMLFactory(book_id=2)

    # No chapters for ids 3 and 4.

    assert BookId.without_reviews() == [3, 4]
