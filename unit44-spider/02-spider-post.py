from urllib import request,parse
import random
import json

# querystring: ?key=value&key2=value2
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

form_data={
"type":"AUTO",
"i": "你",
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
"salt": "15447733457503",
"sign": "2ff6c836adf40639404c20cc21ac7838",
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_REALTIME",
"typoResult": "false"
}

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
#data=parse.urlencode(form_data).encode()

# print(dir(req))
# # 获取请求的完整地址
# print(req.full_url)
# # 获取请求头信息
# print(req.headers['User-agent'])
# print(req.get_header('User-agent'))

#req=request.Request(url,data=data,headers=header)
with request.urlopen(req,json.dumps(form_data).encode('utf-8')) as f:
    data=f.read()

    print(f.status)


    print(data.decode())






