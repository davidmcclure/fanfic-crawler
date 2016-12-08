

from scrapy.item import Item, Field, ItemMeta

from fanfic.models import BookId, Chapter, Metadata


class SQLAlchemyItemMeta(ItemMeta):

    def __new__(meta, name, bases, dct):

        """
        Set item fields from SQLAlchemy columns.
        """

        cls = ItemMeta.__new__(meta, name, bases, dct)

        if cls.model:

            for col in cls.model.__table__.columns:
                cls.fields[col.name] = Field()

        return cls


class SQLAlchemyItem(Item, metaclass=SQLAlchemyItemMeta):

    model = None

    def row(self):

        """
        Make the SQLAlchemy model instance.
        """

        return self.model(**self)


class BookIdItem(SQLAlchemyItem):
    model = BookId


class ChapterItem(SQLAlchemyItem):
    model = Chapter


class MetadataItem(SQLAlchemyItem):
    model = Metadata
