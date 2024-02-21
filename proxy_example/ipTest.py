"""_summary_
Test the usability of IPs
"""


import time
import os 
import pandas as pd
import requests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re, datetime
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, required=True)
    parser.add_argument("--port", type=str, required=True)
    args = parser.parse_args()
    return args 

def test(ip, port):
    #for example: "103.47.93.213:1080"
    proxy = ip + ":" + port
    chrome_options = webdriver.ChromeOptions()
    proxy = "103.47.93.213:1080"
    chrome_options.add_argument(f'--proxy-server={proxy}')
    url = "https://myexternalip.com/raw"
    broswer = webdriver.Chrome(options = chrome_options)
    broswer.get(url)

    while True:
        pass
    

if __name__ == '__main__':
    args = arg_parse()
    ip = args.ip
    port = args.port
    test(ip, port)
