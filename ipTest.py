import time
import os 
import pandas as pd
import requests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re, datetime
import argparse


chrome_options = webdriver.ChromeOptions()
proxy = "103.47.93.213:1080"
chrome_options.add_argument(f'--proxy-server={proxy}')
url = "https://myexternalip.com/raw"
broswer = webdriver.Chrome(options = chrome_options)
broswer.get(url)

while True:
    pass