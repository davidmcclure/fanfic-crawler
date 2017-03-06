

import re

from scrapy import Request

from fanfic.items import ReviewHTMLItem

from .book import BookSpider


class ReviewSpider(BookSpider):

    name = 'review'

    fanfic_prefix = 'r'

    def parse(self, res):
        """Extract reviews, continue to the next page.
        """
        # Extract reviews.

        for tr in res.selector.xpath('//table[@id="gui_table1i"]/tbody/tr'):

            html = tr.extract()

            review_id = int(
                re.search('reviewid=(?P<id>[0-9]+)', html)
                .group('id')
            )

            yield ReviewHTMLItem(
                review_id=review_id,
                book_id=self.book_id,
                html=html,
            )

        # Continue to next page.

        next_href = (
            res.selector
            .xpath('//a[text()="Next »"]/@href')
            .extract_first()
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)
