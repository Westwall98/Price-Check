from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import os
import goods

goods = goods.set()

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
