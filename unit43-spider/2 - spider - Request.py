from urllib import request,parse
import random
url = 'http://www.runoob.com/?'
#查询数据
query_string = {'s':'js'}

#转换成key-value
query_string = parse.urlencode(query_string)
#print(query_string) #s=js
#拼接url
url+=query_string

##用Request类构建了一个完整的请求，增加了headers等一些信息
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]

#随机读取列表
user_agent = random.choice(ua_list)
req.add_header("User-Agent",user_agent)
# print(dir(req))
# # 获取请求的完整地址
# print(req.full_url)
# # 获取请求头信息
#print(req.headers['User-agent'])
# print(req.get_header('User-agent'))

with request.urlopen(req) as f:
    data=f.read()

   # print(f.status)
    with open("菜鸟教程.html","w+",encoding="utf-8") as fp:
        fp.write(data.decode())
    #print(data.decode())
