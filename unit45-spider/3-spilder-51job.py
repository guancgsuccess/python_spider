import re

from pyquery import PyQuery as pq

#地点
#re_address = '<span class="t4">(.*?)</span>'
re_address = '<span class="t2">(.*?)</span>'
red = re.compile(re_address)
lst = []
#re_enterprice = '<span class="t2"><a target="\w*" title="\w*" href="\w*">(.*?)</a></span>'
with open('51job.html','r+',encoding='utf-8') as fp:
    data = fp.read()
    addr = red.findall(data)
    lst.append(addr)
   # print(addr)
   # print(pq.text(addr))
    #print(data)
s = lst[0][1:]
for i in s:
    #print(i)
    p = pq(i)
    d = p('a').text()
    print(d)
#p = pq('<a target="_blank" title="苏州海管家物流科技有限公司" href="https://jobs.51job.com/all/co3854782.html">苏州海管家物流科技有限公司</a>')
#d = p('a').text()  # 返回hello
#print(d)