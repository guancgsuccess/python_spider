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

print(browser.page_source)#拿到的渲染之后的页面 # 模仿人来做


# 需要等待一会 - 才能够拿到数据
#wait = WebDriverWait(browser,10)
#wait.until(EC.presence_of_element_located((By.ID, "content_left")))
browser.implicitly_wait(3)
#time.sleep(3)

with open('51job.html','w+',encoding='utf-8') as fp:
    fp.write(browser.page_source)
    fp.close()