""" Gets drills from screwfix.com"""
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from items import SfixSpiderItem

class SfixSpider(scrapy.Spider):

    name = 'sfix-spider'
    allowed_domains = ['screwfix.com']
    custom_settings = {'FEED_FORMAT':'csv', 'FEED_URI':'drills.csv'}

    start_urls = [
        'https://www.screwfix.com/c/tools/drills/cat830704#category=cat830704'
    ]

              
    def parse(self, response):
        for sf_product in response.xpath("//*[@class='lg-12 md-24 sm-24 cols']"):
            loader = ItemLoader(item=SfixSpiderItem(), 
                selector=sf_product, response=response)
            loader.add_xpath('link', ".//h3[@class='lii__title']/a/@href")
            loader.add_xpath('price', ".//div[@class='lii_price']/h4/text()")
            loader.add_xpath('description', ".//*[@class='lii__title']/a/text()")
            yield loader.load_item()
            
        next_page = response.xpath("//a[@id='next_page_link']/@href").get()
        
        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse)

# main driver #
if __name__ == "__main__":
    # run scraper
    process = CrawlerProcess()
    process.crawl(SfixSpider)
    process.start()




