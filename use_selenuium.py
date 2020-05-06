# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:15:20 2020

@author: zhouxu
"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options #设置静默模式

#chrome_options = Options()#设置静默模式
#chrome_options.add_argument('--headless') #设置静默模式
#driver = webdriver.Chrome(options=chrome_options)#设置静默模式
driver = webdriver.Chrome()
url1 = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/chromedriver/ChromeDriver.html'
driver.get(url1)
time.sleep(1)
botton = driver.find_element_by_tag_name('a')
botton.click()
time.sleep(1)
url2 = 'http://npm.taobao.org/mirrors/chromedriver/2.44/'
driver.get(url2)
time.sleep(1)
button2 = driver.find_element_by_link_text('chromedriver_win32.zip')
#print(button2)
button2.click()
time.sleep(1)
print('成功')
driver.close()