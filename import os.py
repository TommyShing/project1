import os
import re
import json
import time
import requests
from bs4 import BeautifulSoup




TOKEN = ""
PROXIES = {
    "http": "http://127.0.0.1:10808",
    "https": "http://127.0.0.1:10808"
}





headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.116 Safari/537.36",
        "origin": "https://www.google.com"
    }






url = "https://wwww.google.com"
session = requests.Session()
session.get(url, headers=headers)

f = session.post(url, headers=headers)

doc = (f.text)

soup = BeautifulSoup(doc, 'html.parser')

print(soup.prettify())

