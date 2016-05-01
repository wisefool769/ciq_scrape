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

chrome_driver_path = "/usr/local/bin/chromedriver"
cp = ConfigParser()
cp.read("credentials.ini")
settings = cp["defaults"]
username = settings["username"]
password = settings["password"]
sleep_interval = 1



	# if(headless):
		# DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'
		# driver = webdriver.PhantomJS(executable_path='/Users/devin.mancuso/node_modules/phantomjs/bin/phantomjs')
	# else:


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

# driver.set_window_size(1920, 1080)
driver.maximize_window()

url = "https://www.capitaliq.com/CIQDotNet/Login.aspx"
driver.get(url)
driver.find_element_by_id('myLogin_myUsername').send_keys(username)	
driver.find_element_by_id('myLogin_myPassword').send_keys(password)
time.sleep(sleep_interval)
driver.find_element_by_name('myLogin$myLoginButton').click()
time.sleep(sleep_interval)
driver.find_element_by_name('Displaysection1$_assignExpenseCode$AssignExpenseCodeMode').click()
driver.find_element_by_name('Displaysection1$_submitBtn').click()
WatchURL = "https://www.capitaliq.com/CIQDotNet/Lists/Constituents.aspx?listObjectId=321989361"
driver.get(WatchURL)
	
	# hover to Fantasy Basketball to display the hidden dropdown menu 
teams = driver.find_element_by_xpath("//li[@class = 'Navitem Navitem-main Navitem-fantasy Va-top Fl-start Topstart']")
hov = ActionChains(driver).move_to_element(teams)
hov.perform()
time.sleep(sleep_interval)

driver.find_element_by_xpath("//a[text() = '"+ teamname +"']").click()
time.sleep(sleep_interval)


driver.quit()
	
	
base_url = 'https://www.capitaliq.com/'

Comp_link = 'CIQDotNet/Company/Compensation/CompensationSummary'
 
r = requests.get(url_to_scrape)
 
soup = BeautifulSoup(r.text, 'lxml')
 
companies_links = []
ipdb.set_trace()
for table_row in soup.select(".cTbListBody tr"):
	ipdb.set_trace();
	# Each table row has a set of tabel cells, or tds. Let's
	# get all of those.
	table_cells = table_row.findAll('td')

	# Our table has one exception -- a row without any cells.
	# Let's handle that special case here by making sure we
	# have more than zero cells before processing the cells
	if len(table_cells) > 0:
             
		
		# By looking at our source (probably easiest in your browser), we can 
		# see that the link is in the first td of each row. Let's extract the
		# value of that link here.
		#
		# Should this link pattern change, find an archive of an
		# example at http://perma.cc/RTU7-57DL
           relative_link_to_company_details = table_cells[0].find('a')['href']
           CompanyID = relative_link_to_company_details[18:]
            
              

		# The links to the inmates are relative (they look 
		# like Details.aspx?bi=212840). We need to make them absolute links.
		# We do that by prepending our base URL (which conveniently is the same
		# one we used to get the list of inmates.)
           absolute_link_to_company_details = base_url + Comp_link + CompanyID

		# We're done getting the link to the inmate details. Let's add it
		# to our list of inmates for later use
           companies_links.append(absolute_link_to_company_details)

print companies_links    
