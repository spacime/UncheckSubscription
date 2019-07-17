import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

DOMAIN = 'www.quantcast.com/top-sites/US'
URL = 'http://%s' % DOMAIN

class MySpider(scrapy.Spider):
    name = DOMAIN
    allowed_domains = [DOMAIN]
    f = open("Top_Viewed_Websites.txt")

    with open("Top_Viewed_Websites.txt", "rt") as f:
        start_urls = ['http://' + url.strip() for url in f.readlines()[0:100]]
    
    def parse(self, response):
        le = LinkExtractor() # empty for getting everything, check different options on documentation
        for link in le.extract_links(response):
            print link.url
            yield Request(link.url, callback=self.parse)