import requests
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import pymysql


league = "epl_fixtures"

mydb = pymysql.connect(
            host="nfldb2.cke1iobwnywt.us-east-1.rds.amazonaws.com",
            user="des5ve",
            passwd="Cm14fcfire",
            database= "BetTrack"
        )

resultsFull = []
mycursor = mydb.cursor()
sqlQuery = "select Wk, Day, Date, Time, Home, XGHome, Score, xGAway, Away, Venue from " +league
mycursor.execute(sqlQuery)
rows = mycursor.fetchall()
for row in rows:
    results = {}
    results['Wk'] = row[0]
    results['Day'] = row[1]
    results['Date'] = row[2]
    results['Time'] = row[3]
    results['Home'] = row[4]
    results['xGHome'] = row[5]
    results['Score'] = row[6]
    results['xGAway'] = row[7]
    results['Away'] = row[8]
    results['Venue'] = row[9]
    resultsFull.append(results)
    print(results)
