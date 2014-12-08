# -*- coding: cp936 -*-
##################
import urllib,re
def sprider(url, r):
    # page = urllib.urlopen(url)
    # html = page.read()
    # getHtml(url)
    # r=r'<div class="co_content222">.*?</div>'
    # html = unicode(html, "gb2312").encode("utf8")
    s = getHtml(url)
    r = re.compile(r, re.S)
    domList = re.findall(r, s)
    print str(len(domList)) + "====" + url
    if len(domList) == 0:
        return ""
    else:
        return domList[0]


def saveHtmlFile(html):
    path = "d:\\111.html"
    f = open(path, "w")
    f.write(str(html))
    f.close()
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    r=r'gb2312'
    s=html
    # if re.match(r,s):
    if re.findall(r,s)!=[]:
        html=html.decode("gb2312")
        html=html.encode("utf-8")
        # print html
        return html
    elif re.findall("utf-8",s)!=[]:
        html=html.decode("utf-8")
        html=html.encode("utf-8")
        return html
    else:
        return html
xiaopianR = r'<div class="co_content222">.*?</div>'
xiaopianUrl = "http://www.xiaopian.com"
# xiaopianHtml=sprider(xiaopianUrl,xiaopianR,0)
# pin5iR=r'<div class="TabContent">.*?<div>'
pin5iR = r'<div id="myTab0_Content1".*?</div>'
pin5iUrl = "http://www.pin5i.com"
pin5iHtml = sprider(pin5iUrl, pin5iR)
# class="news clearfix"
# print pin5iHtml
csdnR = r'<div class="box hot_blog">.*?</div>'
csdnUrl = "http://www.csdn.net/"
csdnHtml = sprider(csdnUrl, csdnR)
# print csdnHtml
csdnR = r'<div class="news_list">.*?</div>'
csdnHtml2 = sprider(csdnUrl, csdnR)
# print csdnHtml2
csdnDownloadUrl = "http://download.csdn.net/"
csdnDownloadR = r'<div id="tagContent">.*?</div>'
csdnDownloadHtml = sprider(csdnDownloadUrl, csdnDownloadR)
csdnDownloadR = r'<div class="bor_box_1 clear">.*?</div>'
csdnDownloadHtml2 = sprider(csdnDownloadUrl, csdnDownloadR)
# oschinaR = r'<div class="p1">.*</div>'
# oschinaUrl = "http://www.oschina.net"
# oschinaHtml = sprider(oschinaUrl, oschinaR)
jb51R=r'<div class=left>.*?</div>'
jb51Url="http://www.jb51.net/books/"
jb51Html=sprider(jb51Url,jb51R)
# jb51Html=jb51Html.decode("utf-8")
# page = urllib.urlopen(jb51Url)
# html = page.read()
# print html
# zhihuR=r'<div id="zh-recommend">.*?</div>'
# zhihuUrl="http://www.zhihu.com/explore"
# zhihuHtml=sprider(zhihuUrl,zhihuR)
# zhihuR=r'<div class="explore-tab" id="js-explore-tab">.*?</div>'
# zhihuHtml2=sprider(zhihuUrl,zhihuR)

import time
#获得当前时间时间戳
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
saveHtmlFile(
    '<p style="color:red">'+otherStyleTime+'</p>'+
    '<p style="color:red">pin5i</p>' + pin5iHtml +
    '<p style="color:red">csdn</p>' + csdnHtml +
    '<p style="color:red">csdnhot</p>' + csdnHtml2 +
    '<p style="color:red">csdndownload</p>' + csdnDownloadHtml +
    '<p style="color:red">csdndownload2</p>' + csdnDownloadHtml2+
    # '<p style="color:red">oschina</p>'+oschinaHtml
    '<p style="color:red">jb51</p>'+jb51Html
    # '<p style="color:red">知乎</p>'+zhihuHtml+
    # '<p style="color:red">知乎</p>'+zhihuHtml2
)
# open write http://www.xiaopian.com/html/gndy/dyzz/20141206/105582.html
