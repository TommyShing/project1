import json
import logging
import logging.config
import os
import re
import time
from selenium import webdriver

import httpx 



browser = webdriver.Firefox()
browser.maximize_window()

browser.get('https://www.xshellz.com/login')
time.sleep(1)

username = os.environ["USR"]
password = os.environ["PWD"]

acc_input = browser.find_element_by_xpath('//*[@id="username"]')
acc_input.send_keys(username)
pwd_input = browser.find_element_by_xpath('//*[@id="password"]')
pwd_input.send_keys(password)

browser.find_element_by_xpath('//*[@id="remember"]').click()

browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[2]/div/div/div/div/form/button').click()
time.sleep(10)

browser.get('https://www.xshellz.com/xpanel/shell/135211')
time.sleep(10)
browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[11]/div/div/table/tbody/tr[7]/td[2]/div/div[1]/button').click()
time.sleep(10)
