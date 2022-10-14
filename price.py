from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import date
import datetime
import requests
import os

goods = {
    '罗技无线鼠标':'100004546721',
    'NAS':'100014187286',
    'iPhone':'100038004359'
}


chromedriver = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options,service=Service(chromedriver))

for good in goods.keys():
    goodnum = goods[good]
    url = 'https://item.jd.com/{}.html'.format(goodnum)
    driver.get(url)
    price = driver.find_element(By.XPATH,"//span[@class=\"price J-p-{}\"]".format(goodnum))
    print(good + ': ￥' + price.text)
