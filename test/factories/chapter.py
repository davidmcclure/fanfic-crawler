

import factory

from fanfic.services import session
from fanfic.models import Chapter


class ChapterFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Chapter

    book_id = factory.Sequence(
        lambda n: n
    )

    chapter_number = factory.Sequence(
        lambda n: n
    )

    chapter = 'text'
