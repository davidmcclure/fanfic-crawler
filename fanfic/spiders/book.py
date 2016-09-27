

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

        nodes = (
            response
            .xpath('//div[@class="Section1"]/descendant::text()')
            .extract()
        )

        text = ' '.join(nodes)

        yield ChapterItem(text=text)
