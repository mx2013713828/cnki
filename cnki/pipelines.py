# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import CnkiItem
import pymongo
from scrapy.conf import settings

class CnkiPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']#将settings 中定义的数据库的配置提取并连接数据库
        port = settings['MONGODB_PORT']
        #dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(settings["MONGODB_SERVER"],settings["MONGODB_PORT"])#连接mongodb 本地 可以不加参数
        db = client[settings['MONGODB_DBNAME']] #db 等于 连接到mongo后，连接到名为DBNAME的数据库中
        #tdb = client[dbName]
        #self.post = tdb[settings['MONGODB_DOCNAME']]
        self.collection = db[settings['MONGODB_COLLECTION']] #连接到数据库中的collection中（table）

    # 创建process_item 函数  管道中的数据，可以将数据进行筛选等操作  {try exception  或者 if}
    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.collection.insert(bookInfo)
        return item #运行时会输出，可选项
