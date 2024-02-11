
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
    f = open("url/urls.txt", 'r')
    #f_info = open("info.txt", "w")
    
    title_path = """//h1[contains(@slot, 'title')]"""
    content_path = """//div[contains(@class, 'text-neutral-content')]//p"""

    
    for url in f:
        chrome_options = Options()
        chrome_options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
            
        title = driver.find_element(By.XPATH, title_path).text
        content = [c.text for c in driver.find_elements(By.XPATH, content_path)]
        content = "\n".join(content)
        print(title)
        print(content)
        print()

           
        #f_info.write(title)
        #f_info.write('\n')

    
if __name__ == '__main__':
    main()
