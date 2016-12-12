

import pytest

from fanfic.models import BookId

from test.factories import BookIdFactory, MetadataHTMLFactory


pytestmark = pytest.mark.usefixtures('db')


def test_without_chapters():

    BookIdFactory(book_id=1)
    BookIdFactory(book_id=2)
    BookIdFactory(book_id=3)
    BookIdFactory(book_id=4)

    MetadataHTMLFactory(book_id=1)
    MetadataHTMLFactory(book_id=2)

    # No metadata for ids 3 and 4.

    assert BookId.without_metadata() == [3, 4]
