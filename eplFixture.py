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
firstFrame = pd.read_html(url)
frame = firstFrame[0].fillna('')
finalframe = frame.drop(columns = ['Attendance', 'Referee', 'Match Report', 'Notes'])
print (finalframe)




#Code For Extracting Match Reports from table
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

