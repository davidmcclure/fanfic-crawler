

import factory

from fanfic.services import session
from fanfic.models import BookId


class BookIdFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = BookId

    book_id = factory.Sequence(
        lambda n: n
    )
