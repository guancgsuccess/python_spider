from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

from selenium.webdriver.chrome.options import Options

try:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    # 隐式等待
    browser.get("http://www.douban.com")

    # 输入账号密码
    browser.find_element_by_name("form_email").send_keys("849962874@qq.com")
    browser.find_element_by_name("form_password").send_keys("success123")

    # 模拟点击登录
    browser.find_element_by_xpath("//input[@class='bn-submit']").click()

    # 等待3秒
    time.sleep(3)

    # 生成登陆后快照
    browser.save_screenshot("douban.png")
finally:
    browser.close()