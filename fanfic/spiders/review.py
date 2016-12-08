

import re

from scrapy import Spider, Request

from fanfic.items import ReviewItem

from .book import BookSpider


class ReviewSpider(BookSpider):

    name = 'review'

    fanfic_prefix = 'r'

    def parse(self, res):

        """
        Extract reviews, continue to the next page.
        """

        for tr in res.selector.xpath('//table[@id="gui_table1i"]/tbody/tr'):
            print(tr)

        next_href = (
            res.selector
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)
