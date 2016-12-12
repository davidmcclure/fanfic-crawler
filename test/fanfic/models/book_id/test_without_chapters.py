

import pytest

from fanfic.models import BookId

from test.factories import BookIdFactory, ChapterFactory


pytestmark = pytest.mark.usefixtures('db')


def test_without_chapters():

    BookIdFactory(book_id=1)
    BookIdFactory(book_id=2)
    BookIdFactory(book_id=3)
    BookIdFactory(book_id=4)

    ChapterFactory(book_id=1)
    ChapterFactory(book_id=1)

    ChapterFactory(book_id=2)
    ChapterFactory(book_id=2)

    # No chapters for ids 3 and 4.

    assert BookId.without_chapters() == [3, 4]
