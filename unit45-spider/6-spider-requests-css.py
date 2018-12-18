from bs4 import BeautifulSoup

html = BeautifulSoup(open('51job.html',encoding='utf-8'),'lxml')

ts = html.select('p.t1 span a')
print(ts)
for t in ts:
    print(str(t.strinng))