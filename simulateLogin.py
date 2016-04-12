#coding:utf-8
import urllib2
import cookielib
import re

cookie1='target cookie'
headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
           'cookie': cookie1
          }

def visitSinaWeibo():
    url = 'http://weibo.com'
    req = urllib2.Request(url, headers=headers)
    text = urllib2.urlopen(req).read()

    # print the title, check if you login to weibo sucessfully
    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    if r:
        file=open('C:\Users\Ryan\Desktop\sinaCookie.txt','w')
        file.write(r.group(1))


if __name__ == '__main__':
    visitSinaWeibo()