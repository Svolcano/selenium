#coding:utf-8
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import datetime 

from lib.DB import DB
from lib.SQLMgr import SQLMgr
id_count = "email"
id_pwd = "password"
id_submit = 'btn-submit'
count = "775202440@qq.com"
pwd = "55668899"
login_url = "https://accounts.douban.com/login"
driver = webdriver.PhantomJS()
try:
    driver.get(login_url)
    old_url = driver.current_url
    ele_email = driver.find_element_by_id(id_count)
    ele_pwd = driver.find_element_by_id(id_pwd)
    ele_submit = driver.find_element_by_class_name(id_submit)
    ele_email.send_keys(count)
    ele_pwd.send_keys(pwd)
    ele_submit.click()
    new_url =  driver.current_url
    print new_url, old_url
    
except Exception as e:
    print e
finally:
    driver.quit()


