import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.sportsbet_update import SportsbetSpider

process=CrawlerProcess(settings=get_project_settings())
process.crawl(SportsbetSpider)
process.start()