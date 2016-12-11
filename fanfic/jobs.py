

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from billiard import Process
from twisted.internet import reactor


class CrawlerSubprocess(Process):

    def __init__(self, spider, *args, **kwargs):

        """
        Set the spider and arguments.
        """

        super().__init__()

        self.runner = CrawlerRunner(get_project_settings())

        self.spider = spider
        self.args = args
        self.kwargs = kwargs

    def run(self):

        """
        Run the spider.
        """

        deferred = self.runner.crawl(
            self.spider,
            *self.args,
            **self.kwargs
        )

        deferred.addBoth(lambda _: reactor.stop())

        reactor.run()


def crawl(spider, book_id: int):

    """
    Run a spider on a book id.
    """

    proc = CrawlerSubprocess(spider, book_id)

    proc.start()
    proc.join()
