

import re

from scrapy import Spider, Request


class MetadataSpider(Spider):

    name = 'metadata'

    def __init__(self, book_id, *args, **kwargs):

        """
        Set the book id.
        """

        # TODO: Base class.

        super().__init__(*args, **kwargs)

        url = 'https://www.fanfiction.net/s/{}'.format(book_id)

        self.start_urls = [url]

        self.book_id = book_id

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
