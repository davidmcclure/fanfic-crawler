

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from rq.decorators import job

from fanfic.services import redis


def crawl(spider: str, book_id: int):

    """
    Run a spider on a book id.
    """

    proc = CrawlerProcess(get_project_settings())

    proc.crawl(spider, book_id=book_id)

    proc.start()


@job('metadata', connection=redis, timeout=3600)
def crawl_metadata(book_id: int):
    crawl('metadata', book_id)
