#coding:utf-8
import urllib
import urllib2
import re

from random import choice

ipList=['120.76.115.134:80','222.83.14.145:3128','119.188.94.145:80']
thisIp=choice(ipList)

input = raw_input("Please input your key words:")
keyWord=urllib.quote(input)

url='http://search.sina.com.cn/iframe/suggest/index.php?q='+keyWord

headers={
        'Get':url,
        'Host':'search.sina.com.cn',
        'Referer':'http://search.sina.com.cn/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
        }

proxy_support = urllib2.ProxyHandler({'http': 'http://'+thisIp})
opener=urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

req=urllib2.Request(url)
for key in headers:
    req.add_header(key,headers[key])

html=urllib2.urlopen(req).read()
file=open('C:\Users\Ryan\Desktop\lianXC.txt','w')
file.write(html)


