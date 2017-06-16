#coding:utf-8
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import datetime 

from lib.DB import DB
from lib.SQLMgr import SQLMgr


target_url = "http://finance.sina.com.cn/stock/sl/#concept_1"
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(10)
try:
    driver.get(target_url)
    html = driver.page_source
    soup = soup=BeautifulSoup(html,'lxml')
    tbody = soup.find_all('tbody')
    tbody = tbody[1]
    tr_list = tbody.find_all('tr')
    row_data = []
    for tr in tr_list:
        tmp_row = []
        td_list = tr.find_all("td")
        a = td_list[0].a.attrs
        tmp_row.append(a['href'].split('#')[1])
        tmp_row.append(td_list[7].a.attrs['href'].split('/')[-2])
        for td in td_list:
            tmp_row.append(td.get_text())
        tmp_row[2] = tmp_row[2].encode('utf-8')
        tmp_row[9] = tmp_row[9].encode('utf-8')
        tmp_row[9] = tmp_row[9].split(" ")[0]
        tmp_row.append('test')
        tmp_row.append(datetime.datetime.now())
        row_data.append(tmp_row)
    print row_data
    db = DB()
    print db.excutemany(SQLMgr.insert_many(), row_data)
    db.close()
except Exception as e:
    print e
finally:
    driver.quit()


