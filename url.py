"""_summary_
Crawls the url of the posts with the "wall street bank" key word.
Stores the url into info.txt
"""

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

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", type=str, required=False, default="wall street bank")
    parser.add_argument("--use_proxy", type=bool, required=False, default=False)
    parser.add_argument("--time_range", type=str, required=False, default="all")
    parser.add_argument("--order", type=str, required=False, default="")
    args = parser.parse_args()
    return args 

def main(key_word, use_proxy, time_range, order):
    """
    keyword (str)
    use_proxy (bool)
    time_range (str): all, year, month, week, day, hour
    order (str): relevance, hot, top, new, comments  
    """
    
    f = open(f"result/urls.txt", 'w')
    if time_range == None:
        key_word = "+".join(key_word.split())
        url = f"https://www.reddit.com/search/?q={key_word}&type=link"
    else:
        # Specify time range of the posts, for exmale, if time_range == "month",
        # then only search for the url of past month
        key_word = "%20".join(key_word.split())
        url = f"https://www.reddit.com/search/?q={key_word}&type=link&t={time_range}"
        if order:
            url = url + f"&sort={order}"
        
   
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    if use_proxy:
        chrome_options.add_argument(f'--proxy-server={random.choice(ips)}')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    path = """//a[contains(@data-testid, 'post-title-text')]"""
    #Scrape 100 urls for now to not have my ip be blocked
    for i in range(100):
        if i % 20 == 0:
            if use_proxy:
                chrome_options.add_argument(f'--proxy-server={random.choice(ips)}')
            # Find url element using Xpath
            url = driver.find_elements(By.XPATH, path)
            # Scrol to the bottom after every 20 urls
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(5)    
            
        u = url[i].get_attribute("href")
        f.write(u)
        f.write('\n')
        print(u)
    
    
if __name__ == '__main__':
    args = arg_parse()
    key_word = args.keyword
    use_proxy = args.use_proxy
    time_range = args.time_range
    order = args.order
    main(key_word, use_proxy, time_range, order)