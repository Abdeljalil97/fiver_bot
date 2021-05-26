import scrapy
from scrapy.loader import ItemLoader
from fiver.items import FiverItem

class JobPageSpider(scrapy.Spider):
    name = 'job_page'
    allowed_domains = ['www.fiver.com']
    start_urls = ['https://www.fiverr.com/no1brandmaker/do-guest-post-on-tech-blogs']

    def parse(self, response):
        l = ItemLoader(item=FiverItem(), response=response)
        l.add_xpath('gigs',"//div[@class='gig-overview']/h1/text()")        
        l.add_xpath('categories_of_gigs','//div[@class="gig-overview"]/nav/ul/li[1]/span/a/text()')        
        l.add_xpath('categories_of_gigs','//div[@class="gig-overview"]/nav/ul/li[2]/span/a/text()')        
        l.add_xpath('Seller', "//div[@class='username-line']/a/text()")        
        l.add_value('job_url', response.url)        
        l.add_xpath('level',"//div[@class='profile-name']/div/span/div[@class='seller-level']/text()")        
        l.add_xpath('membre_since', "//div[@class='seller-card']/div/ul[@class='user-stats']/li[2]/strong/text()")        
        l.add_xpath('response_time', "//div[@class='seller-card']/div/ul[@class='user-stats']/li[3]/strong/text()")        
        l.add_xpath('last_delivery', "//div[@class='seller-card']/div/ul[@class='user-stats']/li[4]/strong/text()")        
        l.add_xpath('about_seller', "//article/div[@class='inner']/text()")        
        l.add_xpath('languages', '//div[@class="product_name"]')        
        l.add_xpath('location', "//div[@class='seller-card']/div/ul[@class='user-stats']/li[1]/strong/text()")        
        l.add_xpath('basic_package', "(//div[@class='package-content']/header/h3/b[@class='title'])[1]/text()")        
        l.add_xpath('basic_package', "(//div[@class='package-content']/header/h3/span[@class='price'])[1]/text()")        
        l.add_xpath('basic_package', "(//div[@class='package-content']/header/p)[1]/text()")             
        l.add_xpath('basic_package', "(//div[@class='package-content']/article/div/div/b[@class='delivery'])[1]/text()")             
        l.add_xpath('basic_package', "(//div[@class='package-content']/article/div/div/b[@class='revisions'])[1]/text()")             
        l.add_xpath('standard_package', "(//div[@class='package-content']/header/h3/b[@class='title'])[2]/text()")        
        l.add_xpath('standard_package', "(//div[@class='package-content']/header/h3/span[@class='price'])[2]/text()")        
        l.add_xpath('standard_package', "(//div[@class='package-content']/header/p)[2]/text()")             
        l.add_xpath('standard_package', "(//div[@class='package-content']/article/div/div/b[@class='delivery'])[2]/text()")             
        l.add_xpath('standard_package', "(//div[@class='package-content']/article/div/div/b[@class='revisions'])[2]/text()")        
        l.add_xpath('preminuim_package', "(//div[@class='package-content']/header/h3/b[@class='title'])[3]/text()")        
        l.add_xpath('preminuim_package', "(//div[@class='package-content']/header/h3/span[@class='price'])[3]/text()")        
        l.add_xpath('preminuim_package', "(//div[@class='package-content']/header/p)[3]/text()")        
        l.add_xpath('preminuim_package', "(//div[@class='package-content']/article/div/div/b[@class='delivery'])[3]/text()")        
        l.add_xpath('preminuim_package', "(//div[@class='package-content']/article/div/div/b[@class='revisions'])[3]/text()")        
        l.add_xpath('skills', '//div[@class="product_name"]')        
        l.add_xpath('description', "//div[@class='description-content']/text()")        
        l.add_xpath('FAQ', '//div[@class="product_name"]')        
        l.add_xpath('ratings_gigs', '//b[@class="rating-score"][1]/text')        
        l.add_xpath('gigs_reviews', '//span[@class="ratings-count"]/text()')        
        l.add_xpath('rating_breakdown', '//div[@class="product_name"]')        
        l.add_xpath('ralated_tags', "//div[@class='gig-tags-container']/ul/li/a/text()")        
       
        return l.load_item()