from datetime import datetime
from scrapy.spiders import SitemapSpider

class FilteredSitemapSpider(SitemapSpider):
    name = 'filtered_sitemap_spider'
    allowed_domains = ['www.fiverr.com']
    sitemap_urls = ['https://www.fiverr.com/sitemap_gigs.xml.gz']

    def sitemap_filter(self, entries):
        for entry in entries:
            
            yield entry