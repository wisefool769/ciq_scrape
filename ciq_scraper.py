from __future__ import print_function
import ipdb
import selenium
import time
from selenium import webdriver
from configparser import ConfigParser
from bs4 import BeautifulSoup
import traceback


def parse(data):
    soup = BeautifulSoup(data, "html.parser")
    print(soup.prettify())
    
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
        time.sleep(self.sleep_interval)
        self.driver.find_element_by_name('Displaysection1$_assignExpenseCode$AssignExpenseCodeMode').click()
        self.driver.find_element_by_name('Displaysection1$_submitBtn').click()

    def get_comp_data(self): 
        watch_url = "https://www.capitaliq.com/CIQDotNet/Lists/WatchLists.aspx"
        self.driver.get(watch_url)
        time.sleep(self.sleep_interval)
        self.driver.find_element_by_partial_link_text('CBD GI').click()
        self.driver.find_element_by_id('ll_35_112_1936').click()
        self.driver.find_element_by_id('myMarketViewConstituentsDataGrid_CriterionDisplaysection2_myConstituentsDataGrid_CompanyHyperlink1_0').click()
        self.driver.find_element_by_id('ll_7_14_403_top').click()
        return self.driver.page_source
        
    
    def main(self):
        try:
            self.open_browser()
            self.do_login()
            data = self.get_comp_data()
            _ = raw_input("Push any key to quit: ")
            self.driver.quit()
            return data
        except Exception:
            traceback.print_exc()
            _ = raw_input("Push any key to quit: ")
            self.driver.quit()

def main():
    sc = Scraper()
    data = sc.main()
    parse(data)

if __name__ == "__main__":
    main()
