from urllib import request,parse
import random

# querystring: ?key=value&key2=value2

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

formdata={
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


data=parse.urlencode(formdata).encode()

# 随机读取列表
user_agent=random.choice(ua_list)
header={
    "User-Agent":user_agent,
    "cookie":"OUTFOX_SEARCH_USER_ID=383265164@10.169.0.84; JSESSIONID=aaa4t7aCkhEqI61B5rnxw; OUTFOX_SEARCH_USER_ID_NCOO=214017613.40320227; ___rl__test__cookies=1536747585767",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com"
}
req=request.Request(url,data,header)
# req.add_header('User-Agent',user_agent)
with request.urlopen(req) as f:
    data=f.read()

    print(f.status)

    print(data.decode())






