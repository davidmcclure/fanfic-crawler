

import re

from scrapy import Request

from fanfic.items import ChapterItem

from .book import BookSpider


class ChapterSpider(BookSpider):

    name = 'chapter'

    def parse(self, res):

        """
        Collect chapter text, continue to the next page.
        """

        chapter_number = int(
            res.selector
            .xpath('//select[@id="chap_select"]/option[@selected]/@value')
            .extract_first()
        )

        chapter = (
            res.selector
            .xpath('//div[@id="storytextp"]')
            .extract_first()
        )

        yield ChapterItem(
            book_id=self.book_id,
            chapter_number=chapter_number,
            chapter=chapter,
        )

        next_onclick = (
            res.selector
            .xpath('//button[text()="Next >"]/@onclick')
            .extract_first()
        )

        next_href = (
            re.search('\'(?P<url>.*)\'', next_onclick)
            .group('url')
        )

        next_url = res.urljoin(next_href)

        yield Request(next_url)
