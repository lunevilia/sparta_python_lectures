# news.py

from openpyxl import Workbook

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

#sp_nws1 > dl > dd.txt_inline > span._sp_each_source


wb = Workbook()
ws1 = wb.active
ws1.title = "articles"




for ar in articles:
    title = ar.select_one('dl > dt > a').text
    url = ar.select_one('dl > dt > a')['href']
    img = ar.select_one('div > a > img')['src'] # 썸네일
    comp = ar.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')


    ws1.append([title, url, comp, img])

driver.quit()
wb.save(filename='articles.xlsx')

