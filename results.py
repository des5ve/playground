import requests
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql


browser = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
epl = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
browser.get(epl)
html = browser.page_source
soup = BeautifulSoup(html)


matchLinks = []
for link in soup.find_all('a'):
    newLink = link.get('href')
    try:
        if newLink[0:11] == "/en/matches":
            matchLinks.append(newLink)
    except TypeError:
            print ("value error")
    except:
        pass

print (matchLinks)