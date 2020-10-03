from bs4 import BeautifulSoup
from selenium import webdriver
import time

import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B0%B0%EC%9A%B0+%EA%B9%80%EB%AF%BC%EC%84%9D") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thum = soup.select('#imgList > div > a > img')

i = 1

for th in thum:
    img = th['src']
    dload.save(img, f'imgs_homeworks/{i}.jpg')
    i += 1
###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

driver.quit() # 끝나면 닫아주기