import ipdb
import selenium
import time
from selenium import webdriver
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

    def get_comp_data(self): 
        watch_url = "https://www.capitaliq.com/CIQDotNet/Lists/WatchLists.aspx"
        self.driver.get(watch_url)
        self.driver.find_element_by_partial_link_text('Thor PG').click()
        self.driver.find_element_by_id('ll_7_14_403').click()
    
    def main(self):
        try:
            self.open_browser()
            self.do_login()
            self.get_comp_data()
            _ = input("Push any key to quit: ")
            self.driver.quit()
        except Exception:
            _ = input("Push any key to quit: ")
            self.driver.quit()

def main():
    sc = Scraper()
    sc.main()

if __name__ == "__main__":
    main()

	
	

 
 
