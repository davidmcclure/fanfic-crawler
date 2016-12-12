

import factory

from fanfic.services import session
from fanfic.models import ProfileHTML


class ProfileHTMLFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = ProfileHTML

    book_id = factory.Sequence(
        lambda n: n
    )

    html = '<html>'
