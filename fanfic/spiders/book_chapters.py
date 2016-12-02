

from scrapy import Spider, Request

from fanfic.items import BookIdItem


class BookChaptersSpider(Spider):

    name = 'book_chapters'

    # TODO: Parametrize.
    start_urls = ['https://www.fanfiction.net/s/11762850']

    def parse(self, res):

        """
        Collect chapter text, continue to the next page.
        """

        pass
