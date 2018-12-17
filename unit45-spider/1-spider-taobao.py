import re
reg_str = '"raw_title": "(.*?)",'
reg = re.compile(reg_str)

reg_price = '"view_price": "(.*?)",'
rp = re.compile(reg_price)
with open('taopage0.html','r+',encoding='utf-8') as fp:
    data = fp.read()
    s = reg.findall(data)
    price = rp.findall(data)
    print(s)
    print(price)