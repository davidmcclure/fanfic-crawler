

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

        username = (
            res.selector
            .xpath('//div[@id="profile_top"]/a/text()')
            .extract_first()
        )

        summary = (
            res.selector
            .xpath('//div[@id="profile_top"]/div/text()')
            .extract_first()
        )

        raw_metadata = ''.join(
            res.selector
            .xpath('''
                //div[@id="profile_top"]/
                span[position()=last()]//text()
            ''')
            .extract()
        )

        parts = raw_metadata.split('-')

        metadata = dict([
            part.split(':')
            for part in parts
            if ':' in part
        ])

        genres = parts[2]

        characters = parts[3]

        print(metadata)
