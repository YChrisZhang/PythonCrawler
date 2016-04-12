#coding:utf-8
import urllib2
import cookielib
import re

cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open('http://weibo.com/u/5038161234/home?wvr=5&lf=reg')

for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

file=open('C:\Users\Ryan\Desktop\sinaCookie.txt','w')

for item in cookie:
    file.write(item.name)
    file.write(item.value)