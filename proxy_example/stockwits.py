import time
import random 
import os 
import pandas as pd
import requests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re, datetime
import argparse
from configs import ips

input_path = """//span[contains(@class, 'title-text')]"""

url = """https://cryptopanic.com/news/wall-street-memes/"""
chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(5)
inputs = driver.find_elements(By.XPATH, """//span[contains(@class, 'title-text')]""")
text = [input.find_element(By.XPATH, ".//span").text for input in inputs]
print(text)

while True:
    pass 

