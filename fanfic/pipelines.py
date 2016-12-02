

from fanfic.database import session
from fanfic.models import BookId


class SQLAlchemyPipeline(object):

    def process_item(self, item, spider):

        """
        Save a database row.
        """

        session.add(item.row())
        session.commit()
