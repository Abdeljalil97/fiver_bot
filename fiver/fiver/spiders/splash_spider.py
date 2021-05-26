import scrapy
from scrapy_splash import SplashRequest

class SplashSpiderSpider(scrapy.Spider):
    name = 'splash_spider'
    allowed_domains = ['www.fiverr.com']
    def start_requests(self):
        yield scrapy.Request(url="https://www.fiverr.com/no1brandmaker/do-guest-post-on-tech-blogs", callback=self.splash_requests )
    
 
    def splash_requests(self,response):
        script =  """
            function main(splash, args)
                
                assert(splash:go(args.url, headers={headers} ))
                assert(splash:wait(5))
                
                return {
                    
                    html = splash:html(),
                
                }
            end
            """.format(headers=response.headers) 
        yield scrapy.SplashRequest(url="https://www.fiverr.com/no1brandmaker/do-guest-post-on-tech-blogs", callback=self.parse,endpoint= 'execute', args = {'lua_source':script} )

    def parse(self, response):
        print(response.xpath("//div[@class='gig-page-packages-table']/table/tbody/tr"))
