

from scrapy import Spider, Request

from fanfic.items import BookIdItem


class BookChapterSpider(Spider):

    name = 'book_chapter'

    # TODO: Parametrize.
    start_urls = ['https://www.fanfiction.net/s/11762850']

    def parse(self, res):

        """
        Collect chapter text, continue to the next page.
        """

        pass
