# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnkiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    number = scrapy.Field()
    data = scrapy.Field()
    outnumber = scrapy.Field()
    outdata = scrapy.Field()
    sname = scrapy.Field()
    add = scrapy.Field()
    fname = scrapy.Field()
    dadd = scrapy.Field()
    dname = scrapy.Field()
    pnum = scrapy.Field()
    keyword = scrapy.Field()
    pages = scrapy.Field()
    typenum = scrapy.Field()

    pass
