# -*- coding: utf-8 -*-
""" use with sfix spider """
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def remove_nt(value):
    return value.replace("\t",'').replace("\n",'')
    
class SfixSpiderItem(scrapy.Item):

    link = scrapy.Field(
        input_processor = MapCompose(str.strip, remove_nt),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(str.strip, remove_nt),
        output_processor = TakeFirst()
    )
    description = scrapy.Field(
        input_processor = MapCompose(str.strip, remove_nt),
        output_processor = TakeFirst()
    )

