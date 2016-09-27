

from scrapy import Spider


class BookIdsSpider(Spider):

    name = 'book_ids'

    start_urls = [
        'https://www.fanfiction.net/book/Harry-Potter/?r=10&len=60',
    ]

    def parse(self, response):

        """
        Collect book ids, continue to the next page.
        """

        for href in response.css('a.stitle::attr(href)'):

            book_id = href.extract().split('/')[2]

            # TODO: Yield BookId item.
            print(book_id)
