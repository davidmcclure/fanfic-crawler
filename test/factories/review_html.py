

import factory

from fanfic.services import session
from fanfic.models import ReviewHTML


class ReviewHTMLFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = ReviewHTML

    book_id = factory.Sequence(
        lambda n: n
    )

    review_id = factory.Sequence(
        lambda n: n
    )

    html = '<html>'
