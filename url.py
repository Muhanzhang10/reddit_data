
import time
import os 
import pandas as pd
import requests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re, datetime
import argparse


def main():
    f = open(f"url/urls.txt", 'w')
    
    url = "https://www.reddit.com/search/?q=wall+street+bank&type=link"
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    path = """//a[contains(@data-testid, 'post-title-text')]"""
    for i in range(100):
        if i % 20 == 0:
            time.sleep(1)
            url = driver.find_elements(By.XPATH, path)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(5)
            
            
        u = url[i].get_attribute("href")
        f.write(u)
        f.write('\n')
        print(u)
    
    
if __name__ == '__main__':
    main()