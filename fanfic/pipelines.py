

from fanfic.database import session
from fanfic.models import BookId


class BookIdPipeline(object):

    def process_item(self, item, spider):

        """
        Save a book id.
        """

        row = item['model'](**item['fields'])

        session.add(row)

        session.commit()
