

import factory

from fanfic.services import session
from fanfic.models import MetadataHTML


class MetadataHTMLFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = MetadataHTML

    book_id = factory.Sequence(
        lambda n: n
    )

    html = '<html>'
