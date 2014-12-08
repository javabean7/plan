# -*- coding: cp936 -*-
__author__ = 'ASUS'
__author__ = 'ASUS'
import urllib, string

url = "http://dl5.csdn.net/fd.php?i=880782151178741&s=bd6c17593216e000c3ea78bd46fe7ac8"
# urllib.urlretrieve(url)
def aa():
    a = '1234'
    a = 'abc'
    print string.capitalize(a)
    a.title()


def test():
    a = {'1': 'one'}
    a['2'] = 'two'
    print a


def test01():
    print 1
import re,urllib
url="http://www.zhihu.com/explore"
url="http://www.jb51.net"
page = urllib.urlopen(url)
html = page.read()
html=html.decode("gb2312")
# html=html.encode("utf-8")
print html

r=r'gb2312'
s='fdsfds gb23 fdsfdsfds'
print re.findall(r,s)==[]

import time
#获得当前时间时间戳
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print timeArray
print otherStyleTime
