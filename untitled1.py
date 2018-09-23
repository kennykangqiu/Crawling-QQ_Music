# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:07:48 2018

@author: 小康
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import re 
import pymongo
import os
from urllib.parse import quote

keyword = '漂洋过海来看你'

url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=" + quote(keyword)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36'}
headers['Referer'] = 'https://y.qq.com/' 
browser = webdriver.Chrome()

browser.get(url) 
time.sleep(2)
name = browser.find_elements_by_class_name('js_song')[0]

name.click()   

browser.get(browser.current_url)
time.sleep(2)
name = browser.find_element_by_link_text("播放")
name.click()

for handle in browser.window_handles:
    browser.switch_to_window(handle)

print(browser.current_url)
time.sleep(2)

title1 = browser.find_element_by_xpath('//*[@id="h5audio_media"]').get_attribute('src')

print(title1)

response = requests.get(title1)
soup =  BeautifulSoup(response.text,'lxml')
img = requests.get(title1,headers=headers)

path1 = 'kk3111'
path = 'D:\MEIZI\{}'.format(path1)

isExists = os.path.exists(path)
if isExists: 
    os.chdir(path)                
else:
    os.makedirs(path) 
    os.chdir(path) 
#name = 
with open(keyword + '.mp3','wb+') as f:
    f.write(img.content)
#f = open(path + '.mp3','ab')
#f.write(img.content)
#f.close()
print('下载完毕') 