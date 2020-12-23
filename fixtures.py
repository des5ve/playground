import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql

#load phantomJS driver
#change the executable path after you got it installed
browser = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")


epl = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
ligueOne = "https://fbref.com/en/comps/13/schedule/Ligue-1-Scores-and-Fixtures"
laLiga = "https://fbref.com/en/comps/12/schedule/La-Liga-Scores-and-Fixtures"
bundesliga = "https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures"
serieA = "https://fbref.com/en/comps/11/schedule/Serie-A-Scores-and-Fixtures"


def getLeagueFixtures(url, table):
  browser.get(url)
  html = browser.page_source
  soup = BeautifulSoup(html)
  firstFrame = pd.read_html(url)
  frame = firstFrame[0].fillna('')
  finalFrame = frame.drop(columns = ['Attendance', 'Referee', 'Match Report', 'Notes']).rename(columns = {"xG.1": "xGAway", "xG": 'xGHome'})
  gameData = []
  numberOfColumns = finalFrame.shape[1]
  columnNames =  finalFrame.columns.tolist()
  for i, row in finalFrame.iterrows():
    dataRow = []
    iterator = 0
    while iterator < numberOfColumns:
      dataRow.append(row[columnNames[iterator]])
      iterator +=1
    gameData.append(dataRow)
  mydb = pymysql.connect(
    host="nfldb2.cke1iobwnywt.us-east-1.rds.amazonaws.com",
    user="",
    password="",
    database= "BetTrack")
  mycursor = mydb.cursor()
  truncateSQL = "TRUNCATE TABLE " +table
  mycursor.execute(truncateSQL)
  sql = "INSERT INTO " +table+ "(Wk, Day, Date, Time, Home, xGHome, Score, xGAway, Away, Venue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  mycursor.executemany(sql, gameData)
  mydb.commit()
  print (mycursor.rowcount, "record inserted")

getLeagueFixtures(bundesliga, "bundesliga_fixtures")


#Code For Extracting Match Reports from table
"""matchLinks = []
for link in soup.find_all('a'):
    newLink = link.get('href')
    try:
        if newLink[0:11] == "/en/matches":
            matchLinks.append(newLink)
    except TypeError:
            print ("value error")
    except:
        pass
"""

