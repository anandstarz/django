from scrapy.spider import BaseSpider
from scrapy.http import Request
from urlparse import urljoin
from scrapy.selector import HtmlXPathSelector
from mall_uk2.items import MallUk2Item
import inspect
class yelpspider(BaseSpider):
    name="soylp333"
    start_urls=[]
#   allowed_domains=["http://www.yelp.com/"]
    fo = open('ata.csv','r+')
    x=[]
    for i in fo:
	x.append(i)
    for j in range(len(x)):
	start_urls.append(x[j].replace('\n',''))

    filehandle = open('usylp_data.csv','w')
    filehandle.write("Name_of_Business\temail\tAddress\tPhone\tWebsite\n")

   
    def parse(self, response):
        itm=[]
        
        item=MallUk2Item()
        hxs = HtmlXPathSelector(response)


        try:
            item['Name_of_Business']=hxs.select('//span[@itemprop="name"]/text()').extract()[0].encode('utf-8').replace('\xe2','').replace('\x80','').replace('\x99s','').strip()
        except:
            item['Name_of_Business']='Null'

        try:
            item['email']= hxs.select('//meta[@itemprop="email"]/@content').extract()[0].encode('utf-8').strip()
        except:
            item['email']='Null'

        try:
            item['Address']=str(hxs.select('//span[@itemprop="streetAddress"]/text()').extract()).replace("u'","").replace('[','').replace(']','').replace("'","")
        except:
            item['Address']='Null'
        try:
            item['Phone']=hxs.select('//a[@class="button actionCall showOnMobile"]/@href').extract()[0].encode('utf-8').strip()
        except:
            try:
                item['Phone']=hxs.select('//i[@class="icon-phone"]/text()').extract()[0].replace('\n','').encode('utf-8').strip()
            except:
                item['Phone']='Null'
        try:    
            item['Website']=hxs.select('//a[@itemprop="url"]/@href').extract()[0].encode('utf-8').strip()
        except:
	    item['Website']='Null'
     


        self.filehandle.write("%s\t%s\t%s\t%s\t%s\n"%(item['Name_of_Business'],item['email'],item['Address'],item['Phone'],item['Website']))


	itm.append(item)
	return itm

