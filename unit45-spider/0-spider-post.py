from urllib import error
import requests
import random
import json
url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&'

qs = {
    'page_start':60
}

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

try:
    with requests.post(url,qs,user_agent) as f:
        data= f.json()
        print(data)
        with open('dtv.json','w+',encoding='utf-8') as fp:
            #fp.write(str(data))
            json.dump(data,fp) # 区别是文件中的json必须是双引号才能够被解析
            #fp.close()
except error.HTTPError as err:
    print(err)
except error.URLError as err:
    print(err)
except Exception as err:
    print(err)

if __name__ == '__main__':
    with open('dtv.json','r+',encoding='utf-8') as fp:
        douban=json.load(fp)
        print(douban['subjects'])