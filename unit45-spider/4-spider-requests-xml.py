from lxml import etree

# 读取xml文件,结果为xml对象
xml = etree.parse('data.xml')
print(xml) # <lxml.etree._ElementTree object at 0x031017D8>

#titles = xml.xpath('/bookstore/book/title')
#titles = xml.xpath('//book/title')
titles = xml.xpath('//title')
print(len(titles))

for tt in titles:
    print(tt.text)
print('*'*20)

# 选择所有title节点的lang属性值
attrs = xml.xpath('/bookstore//title/@lang')

for a in attrs:
    print(a)

print('*'*20)

#选title属性lang = en的内部值
titles = xml.xpath('/bookstore//title[@lang="en"]')
for t in titles:
    print(t.text)

print('*'*20)

books = []
titles = xml.xpath('/bookstore/book/title')
prices = xml.xpath('/bookstore/book/price')
author = xml.xpath('/bookstore/book/author')

for i in range(len(titles)):
    book = {"title":titles[i].text,"price":prices[i].text,"author":author[i].text}
    books.append(book)

print(books)