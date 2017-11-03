# -*- coding: utf-8 -*-
#爬去知网2014年的专利，自行修改j即可
import scrapy

from cnki.items import CnkiItem


class CnkispiderSpider(scrapy.Spider):

    name = "cnkispider"
    allowed_domains = ["dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?ID=SCPD&subBase=all"]
    #专利号按顺序排列 专利尾号分为A,S,U，起始地址设为302697180S,103483317A,203369100U
    start_urls = ['http://dbpub.cnki.net/Grid2008/Dbpub/Detail.aspx?DBName=SCPD2010&FileName=CN'+str(j)+'A&QueryID=4&CurRec=1' for j in range(103483317, 104199988)]

    def parse(self, response):

        name = response.css('td[width="832"]::text').extract_first()
        cnki = response.css('#box')
        all = cnki.css('td[bgcolor="#FFFFFF"]::text').extract()
        item = CnkiItem()
        item['name'] = name
        item['number'] = all[0]
        item['data'] = all[1]
        item['outnumber'] = all[2]
        item['outdata'] = all[3]
        item['sname'] = all[4]
        item['add'] = all[5]
        item['fname'] = all[7]
        item['dadd'] = all[11]
        item['dname'] = all[12]
        item['pnum'] = all[14]
        item['keyword'] = all[15]
        item['pages'] = all[17]
        item['typenum'] = all[18]
        yield item
        #for i in range(302697180,303060980):
         #   url = 'http://dbpub.cnki.net/Grid2008/Dbpub/Detail.aspx?DBName=SCPD2010&FileName=CN'+str(i)+'S&QueryID=4&CurRec=1'
          #  yield scrapy.Request(url=url, callback=self.parse)