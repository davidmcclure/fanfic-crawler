

import re

from scrapy import Spider, Request

from fanfic.items import ChapterItem


class BookSpider(Spider):

    name = 'book'

    # TODO|dev
    start_urls = [
        'https://www.fanfiction.net/s/196188',
    ]

    def parse(self, response):

        """
        Collect text, continue to the next chapter.
        """

        # Get text content.

        nodes = (
            response
            .xpath('//div[@class="Section1"]/descendant::text()')
            .extract()
        )

        text = ' '.join(nodes)

        yield ChapterItem(text=text)

        # Continue to next chapter.

        next_onclick = (
            response
            .xpath('//button[text()="Next >"]/@onclick')
            .extract_first()
        )

        next_rel_url = (
            re.search('\'(?P<url>.*)\'', next_onclick)
            .group('url')
        )

        next_url = response.urljoin(next_rel_url)

        yield Request(next_url, callback=self.parse)
