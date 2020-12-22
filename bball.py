import requests
import json
from requests.auth import HTTPBasicAuth
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

statDictionary = {
    "effectiveFieldGoalPercent": "https://www.teamrankings.com/ncaa-basketball/stat/effective-field-goal-pct",
    
}