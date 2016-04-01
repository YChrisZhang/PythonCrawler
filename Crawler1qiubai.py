# -*- coding:utf-8 -*-
import urllib
import urllib2
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#values={}
headers66 = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers=headers66)
    response = urllib2.urlopen(request)
    page = response.read()
    file=open('C:\Users\Ryan\Desktop\qiubai.txt','w')
    file.write(page)
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason