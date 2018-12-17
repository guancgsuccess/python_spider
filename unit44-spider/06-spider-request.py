import requests
import random

url = 'https://www.liepin.com/suzhou/zhaopin/?dqs=060080&' \
      'salary=&isAnalysis=true&init=1&searchType=1&fromSearchBtn=1&' \
      'jobTitles=&industries=&industryType=&d_headId=cf381555d0d32f6f84e096ca2d76c59c&' \
      'd_ckId=cf381555d0d32f6f84e096ca2d76c59c&d_sfrom=search_city&d_pageSize=40&siTag=&'

#拼接查询参数
qs={
    "key":"python",
    "d_curPage":0
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

headers={
    "user-agent":user_agent
}

with requests.get(url=url,params=qs,headers=headers) as f:
     data=f.text
     with open('python.html','w+',encoding='utf-8') as fp:
         fp.write(data)
         fp.close()

    #print(f.headers['date'])