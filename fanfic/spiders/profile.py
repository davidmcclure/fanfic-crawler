

import time

from fanfic.items import ProfileHTMLItem

from .book import BookSpider


class ProfileSpider(BookSpider):

    name = 'profile'

    def parse(self, res):
        """Extract book metadata fields.
        """
        profile = (
            res.selector
            .xpath('//div[@id="profile_top"]')
            .extract_first()
        )

        yield ProfileHTMLItem(
            book_id=self.book_id,
            html=profile,
        )

    def closed(self, *args, **kwargs):
        """Pause before closing, to throttle requests when the spider is run
        serially by a job queue.
        """
        super().closed(*args, **kwargs)

        time.sleep(2)
