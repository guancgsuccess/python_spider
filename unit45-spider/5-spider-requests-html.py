import lxml.html
etree = lxml.html.etree

parse = etree.HTMLParser(encoding='utf-8')
html = etree.parse('51job.html',parse)
result = etree.tostring(html,encoding='utf-8').decode('utf-8')
#print(html) # <lxml.etree._ElementTree object at 0x0287B0D0>
print(result)

# 找出岗位名称
jobinfos = []
jobs = html.xpath('//p[@class="t1"]/span/a')
print(len(jobs))
for i in range(len(jobs)):

    job = {"job":jobs[i].text.strip()}
    jobinfos.append(job)

print(jobinfos)
