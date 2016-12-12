

from fanfic.singletons import session


class SQLAlchemyPipeline(object):

    def process_item(self, item, spider):

        """
        Save a database row.
        """

        session.add(item.row())
        session.commit()

        return item
