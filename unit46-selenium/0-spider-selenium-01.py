from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

# 模拟搜索
input = browser.find_element_by_id('kw')
input.send_keys('python')
input.send_keys(Keys.ENTER)

print(browser.page_source)#拿到的渲染之后的页面 # 模仿人来做


# 需要等待一会 - 才能够拿到数据
wait = WebDriverWait(browser,10)
#wait.until(EC.presence_of_element_located((By.ID, "content_left")))

time.sleep(3)

with open('baidu.html','w+',encoding='utf-8') as fp:
    fp.write(browser.page_source)
    fp.close()