import logging
from collections import namedtuple
from grab.spider import Spider, Task


#-- Results Items ------------------------------------------------------------#
Film = namedtuple('Film', ['title', 'url', 'rank', 'year'])


#-- Base Spider --------------------------------------------------------------#
class BaseSpider(Spider):
    def do_run(self, **kwargs):
        self.config = kwargs
        self.result_set = set()
        self.run()
        return self.result_set


#-- Movie Spiders ------------------------------------------------------------#
class IMDBSpider(BaseSpider):
    base_url = 'http://www.imdb.com'
    initial_urls = ['http://www.imdb.com/chart/top']

    def task_initial(self, grab, task):

        elements = grab.doc.select('//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr')

        for i, row in enumerate(elements):
            url = row.select('td[2]/a').attr('href')
            rank = i + 1
            self.add_task(Task('page', url=url, rank=rank))

    def task_page(self, grab, task):
        title = grab.doc.select('//*[@id="overview-top"]/h1/span[1]').text()

        if grab.doc.select('//*[@id="overview-top"]/h1/span[3]/a'):
            year = grab.doc.select('//*[@id="overview-top"]/h1/span[3]/a').text()
        else:
            year = grab.doc.select('//*[@id="overview-top"]/h1/span[2]/a').text()

        film = Film(title, grab.response.url, task.rank, year)
        self.result_set.add(film)


class MetaCriticSpider(BaseSpider):
    base_url = 'http://www.metacritic.com/'

    def task_generator(self):
        for i in range(3):
            yield Task('results', url='http://www.metacritic.com/browse/movies/score/metascore/all/filtered?page={}'.format(i))

    def task_results(self, grab, task):
        elements = grab.doc.select('//*[@id="main"]/div[1]/div[1]/div[2]/div[2]/div/div/div')
        for row in elements:
            rank = row.select('div[1]').text().replace('.', '')
            title = row.select('div[3]/a').text()
            url = row.select('div[3]/a').attr('href')
            self.add_task(Task('movie', url=url, title=title, rank=rank))

    def task_movie(self, grab, task):
        if grab.doc.select('//*[@id="main"]/div/div[1]/div[2]/ul/li[2]/span[2]'):
            date = grab.doc.select('//*[@id="main"]/div/div[1]/div[2]/ul/li[2]/span[2]').text()
        else:
            date = grab.doc.select('//*[@id="main"]/div/div[1]/div[2]/ul/li/span[2]').text()

        year = date[-4:].strip()

        film = Film(task.title, grab.response.url, task.rank, year)
        self.result_set.add(film)
