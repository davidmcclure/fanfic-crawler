

from scrapy import Item, Field


class SqlItem(Item):

    model = Field()

    fields = Field()

    def row(self):
        return self['model'](**self['fields'])
