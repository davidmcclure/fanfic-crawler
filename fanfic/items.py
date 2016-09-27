

from scrapy import Item, Field


# TODO: BookItem, with metadata?
class BookIdItem(Item):
    id = Field()


class ChapterItem(Item):
    text = Field()
