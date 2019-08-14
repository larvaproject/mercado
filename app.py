import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mercadoLibre.spiders.spider import MercadoSpider

if __name__ == '__main__':
	process = CrawlerProcess(get_project_settings())

	process.crawl(MercadoSpider)
	process.start()