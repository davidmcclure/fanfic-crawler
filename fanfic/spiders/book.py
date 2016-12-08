

from scrapy import Spider


class BookSpider(Spider):

    fanfic_prefix = 's'

    def __init__(self, book_id, *args, **kwargs):

        """
        Parametrize from a book id.
        """

        super().__init__(*args, **kwargs)

        url = 'https://www.fanfiction.net/{}/{}/'.format(
            self.fanfic_prefix, book_id
        )

        self.start_urls = [url]

        self.book_id = book_id
