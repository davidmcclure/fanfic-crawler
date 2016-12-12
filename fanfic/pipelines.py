

from fanfic.services import session


class SQLAlchemyPipeline(object):

    def process_item(self, item, spider):

        """
        Save a database row.
        """

        session.add(item.row())

        return item
