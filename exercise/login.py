# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'C:\Users\cliff\Downloads\chromedriver_win32\chromedriver.exe')
browser.get('https://www.linkedin.com/')

elem = browser.find_element_by_name("session_key") #寻找账号输入框
elem.clear()
elem.send_keys("xiesiyaocom@163.com") #输入账号
password = browser.find_element_by_name('session_password') #寻找密码输入框
password.clear()
password.send_keys("1") #输入密码
elem.send_keys(Keys.RETURN) #模拟键盘回车键
time.sleep(10) #大家这里可以直接sleep, 也可以使用上一课讲到的等待某个条件出现
print(browser.page_source)
browser.close() #在视频中，这一行会被注释掉，以方便观察结果

