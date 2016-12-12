

import time

from fanfic.items import MetadataHTMLItem

from .book import BookSpider


class MetadataSpider(BookSpider):

    name = 'metadata'

    def parse(self, res):

        """
        Extract book metadata fields.
        """

        metadata = (
            res.selector
            .xpath('//div[@id="profile_top"]')
            .extract_first()
        )

        yield MetadataHTMLItem(
            book_id=self.book_id,
            html=metadata,
        )

    def closed(self):

        """
        Pause before closing, to throttle requests when the spider is run
        serially by a job queue.
        """

        time.sleep(self.settings['DOWNLOAD_DELAY'])
