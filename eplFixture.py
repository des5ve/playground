import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#load phantomJS driver
#change the executable path after you got it installed
browser = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")


url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"

browser.get(url)
html = browser.page_source
#print(html)
soup = BeautifulSoup(html)
print (pd.read_html(url))

for link in soup.find_all('a'):
    newLink = link.get('href')
    if newLink[0:10] == "/en/matches":
        print ("true")