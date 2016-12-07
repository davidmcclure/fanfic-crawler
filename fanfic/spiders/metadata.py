

import re

from scrapy import Spider, Request

from .book import BookSpider


class MetadataSpider(BookSpider):

    name = 'metadata'

    def parse(self, res):

        """
        Extract book metadata fields.
        """

        title = (
            res.selector
            .xpath('//div[@id="profile_top"]/b/text()')
            .extract_first()
        )

        print(title)
