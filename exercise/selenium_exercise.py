# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

browser = webdriver.Chrome(r'C:\Users\cliff\Downloads\chromedriver_win32\chromedriver.exe')
browser.get("http://www.taobao.com")
input_first = browser.find_element(By.ID,"q")
print(input_first)
browser.close()