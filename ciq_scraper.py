# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import ipdb
import requests
import selenium
from bs4 import BeautifulSoup
import time
#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import argv
import click
import sys

from configparser import ConfigParser

class Scraper(object):
    def __init__(self):
        chrome_driver_path = "/usr/local/bin/chromedriver"
        cp = ConfigParser()
        cp.read("credentials.ini")
        settings = cp["defaults"]
        self.username = settings["username"]
        self.password = settings["password"]
        self.sleep_interval = 1
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

    def open_browser(self):
        self.driver.maximize_window()
        url = "https://www.capitaliq.com/CIQDotNet/Login.aspx"
        self.driver.get(url)

    def do_login(self):
        self.driver.find_element_by_id('myLogin_myUsername').send_keys(self.username)	
        self.driver.find_element_by_id('myLogin_myPassword').send_keys(self.password)
        time.sleep(self.sleep_interval)
        self.driver.find_element_by_name('myLogin$myLoginButton').click()
        time.sleep(sleep_interval)
        self.driver.find_element_by_name('Displaysection1$_assignExpenseCode$AssignExpenseCodeMode').click()
        self.driver.find_element_by_name('Displaysection1$_submitBtn').click()
    
    def main(self):
        try:
            self.open_browser()
            self.do_login()
            self.driver.quit()
        except Exception:
            self.driver.quit()

def main():
    sc = Scraper()
    sc.main()

if __name__ == "__main__":
    main()

 
 
