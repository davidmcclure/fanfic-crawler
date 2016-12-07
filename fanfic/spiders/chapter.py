

import re

from scrapy import Spider, Request

from fanfic.items import ChapterItem


class ChapterSpider(Spider):

    name = 'chapter'

    def __init__(self, book_id, *args, **kwargs):

        """
        Set the book id.
        """

        super().__init__(*args, **kwargs)

        url = 'https://www.fanfiction.net/s/{}'.format(book_id)

        self.start_urls = [url]

        self.book_id = book_id

    def parse(self, res):

        """
        Collect chapter text, continue to the next page.
        """

        chapter_number = int(
            res.selector
            .xpath('//select[@id="chap_select"]/option[@selected]/@value')
            .extract_first()
        )

        content = (
            res.selector
            .xpath('//div[@id="storytextp"]')
            .extract_first()
        )

        yield ChapterItem(
            book_id=self.book_id,
            chapter_number=chapter_number,
            content=content,
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
