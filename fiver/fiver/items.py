# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FiverItem(scrapy.Item):
    gigs = scrapy.Field()
    categories_of_gigs = scrapy.Field()
    Seller = scrapy.Field()
    job_url = scrapy.Field()
    level = scrapy.Field()
    membre_since = scrapy.Field()
    last_delivery = scrapy.Field()
    about_seller = scrapy.Field()
    languages = scrapy.Field()
    location = scrapy.Field()
    package = scrapy.Field()
    skills = scrapy.Field()
    description = scrapy.Field()
    basic_package = scrapy.Field()
    standard_package = scrapy.Field()
    preminuim_package = scrapy.Field()
    FAQ = scrapy.Field()
    ratings_gigs = scrapy.Field()
    gigs_reviews = scrapy.Field()
    rating_breakdown = scrapy.Field()
    response_time = scrapy.Field()
    ralated_tags = scrapy.Field()
    
