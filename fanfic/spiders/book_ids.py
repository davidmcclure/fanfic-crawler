

from scrapy import Spider, Request

from fanfic.items import SqlItem
from fanfic.models import BookId


class BookIdsSpider(Spider):

    name = 'book_ids'

    start_urls = [
        'https://www.fanfiction.net/book/Harry-Potter/?r=10&len=60',
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'fanfic.pipelines.BookIdPipeline': 100,
        }
    }

    def parse(self, res):

        """
        Collect book ids, continue to the next page.
        """

        # Generate books ids.

        for href in res.xpath('//a[@class="stitle"]/@href').extract():

            book_id = int(href.split('/')[2])

            yield SqlItem(model=BookId, fields=dict(book_id=book_id))

        # Continue to next page.

        next_href = (
            res
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)
