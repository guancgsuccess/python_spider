from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.51job.com/")

# 模拟搜索
input = browser.find_element_by_id('kwdselectid')
input.send_keys('java')
#input.send_keys(Keys.ENTER)

# 点击事件
button = browser.find_element_by_class_name('top_wrap').find_element_by_tag_name('button')
button.click()

print("句柄:",browser.window_handles)

#print(browser.page_source)#拿到的渲染之后的页面 # 模仿人来做
# 打印出搜索结果页的ip地址
# print(browser.current_url)

# 再次请求搜索结果页
search_url = browser.current_url
browser.get(search_url)

#遍历出页面中48个带有超链接的图片，可以进入查看详情页

#browser.implicitly_wait(3)

#time.sleep(5)

a_links = browser.find_elements_by_xpath('//p[@class="t1 "]/span/a')
#a_links = browser.find_elements_by_class_name('t1').find_element_by_tag_name('span')
# a_links = browser.find_element_by_class_name('t1')
print(len(a_links))

for i in range(len(a_links)):
    a_links = browser.find_elements_by_xpath('//p[@class="t1 "]/span/a')
    a_links[i].click()
    browser.implicitly_wait(1)
    #time.sleep(5)
    with open('java_{0}.html'.format(i), 'w+',encoding='utf-8') as fp:
        #browser.get(browser.current_url)
        #print(a_links[i].get_attribute('href'))

        # 获取每个链接的url
        a_url = a_links[i].get_attribute('href')
        browser.get(a_url)

        #print(browser.current_url)
        data=browser.page_source
        print(browser.current_url)
        #print(data)
        fp.write(data)
        fp.close()
    browser.get(search_url)

