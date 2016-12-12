

from scrapy import Spider, Request

from fanfic.items import BookIdItem
from fanfic.services import session


class BookIdSpider(Spider):

    name = 'book_id'

    # Rating: All, >60k words, English
    start_urls = [(
        'https://www.fanfiction.net/book/Harry-Potter/'
        '?&srt=1&lan=1&r=10&len=60'
    )]

    def parse(self, res):

        """
        Collect book ids, continue to the next page.
        """

        # Generate books ids.

        for href in res.xpath('//a[@class="stitle"]/@href').extract():

            book_id = int(href.split('/')[2])

            yield BookIdItem(book_id=book_id)

        # Continue to next page.

        next_href = (
            res
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)

        # Flush book ids en-route.

        session.commit()
