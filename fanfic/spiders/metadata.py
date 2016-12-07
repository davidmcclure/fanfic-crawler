

import re

from scrapy import Spider, Request

from fanfic.utils import href_to_id

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

        user_id = href_to_id(
            res.selector
            .xpath('//div[@id="profile_top"]/a/@href')
            .extract_first()
        )

        print(user_id)
