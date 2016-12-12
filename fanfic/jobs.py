

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def crawl(spider: str, book_id: int):

    """
    Run a spider on a book id.
    """

    proc = CrawlerProcess(get_project_settings())

    proc.crawl(spider, book_id=book_id)

    proc.start()
