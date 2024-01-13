# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    Faculty = scrapy.Field()
    Major = scrapy.Field()
    Title = scrapy.Field()
    Supplier = scrapy.Field()
    Additional = scrapy.Field()

