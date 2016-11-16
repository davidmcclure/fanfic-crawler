

from scrapy import Item, Field


class BookIdItem(Item):
    id = Field()


class ChapterItem(Item):
    text = Field()
