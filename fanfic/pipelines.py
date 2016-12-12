

from fanfic.services import session


class SQLAlchemyPipeline(object):

    def process_item(self, item, spider):

        """
        Save a database row.
        """

        session.add(item.row())
        return item

    def close_spider(self, spider):

        """
        Commit the session when the crawl finishes.
        """

        session.commit()
