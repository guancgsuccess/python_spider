import lxml.html
from urllib import request
from PIL import Image
from io import BytesIO
etree = lxml.html.etree
import requests


parse = etree.HTMLParser(encoding='utf-8')
html = etree.parse('lianyi.html',parse)
print(dir(request))

imgs = html.xpath('//div[@class="warp"]//img/@src')
print(imgs)
count = 0
for i in imgs:
    #request.urlretrieve(i, 'imgs/'+i)
    response = requests.get(i)
    image = Image.open(BytesIO(response.content))
    count+=1
    path = "imgs/"+str(count)+".jpg"
    image.save(path)
    #print(dir(i))
    # print(i)
    # with open("/img/"+i,'wb+') as fp:
    #     fp.write(i)
    #     fp.close()
    #print(dir(i))
    #print(i.tail)

# for i in range(len(jobs)):
#
#     job = {"job":jobs[i].text.strip()}
#     jobinfos.append(job)
#
# print(jobinfos)
