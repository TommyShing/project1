import json
import logging
import logging.config
import os
import re
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
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

r = requests.get('https://www.xshellz.com/login')

html_doc = (r.text)

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

