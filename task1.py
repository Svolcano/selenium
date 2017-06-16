#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lib.DB import DB
from lib.SQLMgr import SQLMgr

target_url = "http://finance.sina.com.cn/stock/sl/#concept_1"
driver = webdriver.Chrome()
driver.get(target_url)
web_data = []
try:
    element = WebDriverWait(driver, 10).until(
       EC.presence_of_all_elements_located((By.TAG_NAME,"tr"))                                      
    )
    for tr in element[2:]:
        tr_text = tr.text
        alist = tr.find_elements_by_tag_name("a")
        n1 = alist[0].get_attribute("href")
        n2 = alist[1].get_attribute("href")
        web_data.append([tr_text, n1, n2])
finally:
    driver.quit()

print web_data
#===============================================================================
# db = DB()
# print db.excutemany(SQLMgr.insert_many(), web_data)
# db.close()
#===============================================================================