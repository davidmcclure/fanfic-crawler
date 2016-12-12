

import pytest

from fanfic.models import BookId

from test.factories import BookIdFactory, ProfileHTMLFactory


pytestmark = pytest.mark.usefixtures('db')


def test_without_chapters():

    BookIdFactory(book_id=1)
    BookIdFactory(book_id=2)
    BookIdFactory(book_id=3)
    BookIdFactory(book_id=4)

    ProfileHTMLFactory(book_id=1)
    ProfileHTMLFactory(book_id=2)

    # No metadata for ids 3 and 4.

    assert BookId.without_profiles() == [3, 4]
