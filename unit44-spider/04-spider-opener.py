from urllib import request,parse,error
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#构建一个HTTPHandler处理器对象,支持处理HTTPS请求
http_handler = request.HTTPSHandler(debuglevel=1)
#创建支持处理HTTP请求的oepner对象
opener = request.build_opener(http_handler)

# querystring: ?key=value&key2=value2
url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&'

qs = {
    'page_start':60
}

url = url + parse.urlencode(qs)

req=request.Request(url)

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

# 随机读取列表
user_agent=random.choice(ua_list)
req.add_header('User-Agent',user_agent)



try:
    with opener.open(req) as f:
        data= f.read()
        print(data)
        with open('dtv.json','w',encoding='utf-8') as fp:
            fp.write(data.decode())
except error.HTTPError as err:
    pass
except error.URLError as err:
    pass
except Exception as err:
    pass

