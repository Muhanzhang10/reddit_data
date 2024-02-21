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

import configs


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use_proxy", type=bool, required=False, default=False)
    args = parser.parse_args()
    return args 

def click_more_comment_buttons(driver):
    #class = invisible
    open_more_comment_buttons_path = """
    //faceplate-partial[contains(@loading, "action")]//button[not(contains(@class, 'invisible')) and not(contains(@aria-label, 'Loading'))]
    """
    for i in range(3):
        buttons = driver.find_elements(By.XPATH, open_more_comment_buttons_path)
        for button in buttons:
            try:
                button.click()
            except:
                continue 
    return driver
    

def find_comment(driver, num):
    driver = click_more_comment_buttons(driver)
    result = {"title": [], "content": [], "date": [], "username": [], "layer": []}
    comment_path = """//shreddit-comment"""
    comment2_path = """.//div[contains(@slot, 'comment')]//p"""
    hierarchy = []
    chunks = driver.find_elements(By.XPATH, comment_path)
    for chunk in chunks:
        try:
            username = chunk.get_attribute("author")
        except:
            username = "[deleted]"
        depth = int(chunk.get_attribute("depth"))
        date = chunk.find_element(By.XPATH, ".//time").get_attribute("datetime")
        texts = chunk.find_elements(By.XPATH, comment2_path)
        texts = [text.text for text in texts]
        texts = "\n".join(texts)
        
        # Assumes that the comment tree is in DFS order
        depth += 1
        if depth > len(hierarchy):
            hierarchy.append("1")
        elif depth <= len(hierarchy):
            hierarchy = hierarchy[:depth]
            hierarchy[-1] = str(int(hierarchy[-1]) + 1)
            
        layer = str(num) + "." + ".".join(hierarchy)
        result["title"].append("")
        result["layer"].append(layer)
        result["username"].append(username)
        result["date"].append(date)
        result["content"].append(texts)
        
    return result

#Combine two dictionaries
def combine_result(res1, res2):
    for key in res1:
        res1[key] = res1[key] + res2[key]
    return res1 
    
def main(use_proxy):
    f = open("result/urls.txt", 'r')
    result_df = {"title": [], "content": [], "date": [], "username": [], "layer": []}
    title_path = """//h1[contains(@slot, 'title')]"""
    content_path = """//div[contains(@class, 'text-neutral-content')]//p"""
    username_path = """//a[contains(@class, "author")]"""
    post_time_path = """//time"""
    num = 0
    
    for url in f:
        if use_proxy:
            driver = webdriver.Chrome(seleniumwire_options = configs.OPTIONS)
        else:
            driver = webdriver.Chrome(options=Options())
    
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
        result_df["layer"].append(str(num))
        num += 1
        comment_result = find_comment(driver, num)
        result_df = combine_result(result_df, comment_result)
        
        
    result_df = pd.DataFrame(result_df)
    result_df.to_csv("info.csv", index=False)
    
if __name__ == '__main__':
    args = arg_parse()
    use_proxy = bool(args.use_proxy)
    if use_proxy == "True":
        use_proxy = True 
    else:
        use_proxy = False 
    main(use_proxy)
