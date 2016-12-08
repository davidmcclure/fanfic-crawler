

import re

from scrapy import Spider, Request

from fanfic.items import ReviewItem
from fanfic.utils import extract_int

from .book import BookSpider


class ReviewSpider(BookSpider):

    name = 'review'

    fanfic_prefix = 'r'

    def parse(self, res):

        """
        Extract reviews, continue to the next page.
        """

        # Extract reviews.

        for tr in res.selector.xpath('//table[@id="gui_table1i"]/tbody/tr'):

            review = tr.xpath('.//div/text()').extract_first()

            small = tr.xpath('.//small//text()').extract()

            chapter = ''.join(small).split('.')[0]

            chapter_number = extract_int(chapter)

            xutime = tr.xpath('.//span/@data-xutime').extract_first()

            print(xutime)

        # Continue to next page.

        next_href = (
            res.selector
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)
