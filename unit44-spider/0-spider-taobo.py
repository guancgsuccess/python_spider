from urllib import request,parse

import random
import ssl
import string
ssl._create_default_https_context = ssl._create_unverified_context

ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
def loadData(start,end):
    for i in range(start,end+1):
        taobaoSpider(i)
def taobaoSpider(i):
    qs={
        "s":i*48
    }
    url='https://s.taobao.com/search?q=手机&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=' \
         'tbindexz_20170306&p4ppushleft=5%2C48&'

   # url = "https://s.taobao.com/list?spm=a217f.8051907.312344.2.7e383308OlmjDv&q=T%E6%81%A4&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&"

    url=url+parse.urlencode(qs)
    url = parse.quote(url, safe=string.printable)
    req = request.Request(url)


    # 随机读取列表
    user_agent = random.choice(ua_list)
    req.add_header('User-Agent', user_agent)

    with request.urlopen(req) as f:
        if f.status==200:
            data=f.read().decode("gbk")

            filename='taopage'+str(i)+'.html'
            saveFile(filename,data)



def saveFile(filename,data):
    try:
        with open(filename,'w+',encoding="utf-8") as f:
            f.write(data)
            f.close()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    start=0
    end=1

    loadData(start,end)



