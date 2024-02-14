"""_summary_
Goes to the crawled url of posts and crawl the title and content.
Stores the content in info.txt
TODO: crawl comment contents
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
    parser.add_argument("--use_proxy", type=int, required=False, default=False)
    args = parser.parse_args()
    return args 


def main(use_proxy):
    f = open("result/urls.txt", 'r')
    result_df = {"title": [], "content": [], "date": [], "username": []}
    title_path = """//h1[contains(@slot, 'title')]"""
    content_path = """//div[contains(@class, 'text-neutral-content')]//p"""
    username_path = """//a[contains(@class, "author")]"""
    post_time_path = """//time"""

    
    for url in f:
        chrome_options = Options()
        chrome_options.page_load_strategy = 'eager'
        if use_proxy:
            chrome_options.add_argument(f'--proxy-server={random.choice(random.choice(ips))}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
    
        title = driver.find_element(By.XPATH, title_path).text
        content = [c.text for c in driver.find_elements(By.XPATH, content_path)]
        content = "\n".join(content)

        try: 
            user_name = driver.find_element(By.XPATH, username_path).text
        except:
            user_name = "[deleted]"
            
        post_time = driver.find_element(By.XPATH, post_time_path).get_attribute("datetime")
        result_df["title"].append(title)
        result_df["content"].append(content)
        result_df["date"].append(post_time)
        result_df["username"].append(user_name)
        
    result_df = pd.DataFrame(result_df)
    result_df.to_csv("info.csv")
    
if __name__ == '__main__':
    args = arg_parse()
    use_proxy = args.use_proxy
    main(use_proxy)
