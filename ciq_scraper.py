from __future__ import print_function
import pickle
import ipdb
import selenium
import time
from selenium import webdriver
from configparser import ConfigParser
from bs4 import BeautifulSoup
import traceback
import codecs

def parse(data):
    soup = BeautifulSoup(data, "html.parser")
    file = codecs.open("out.txt", "w", "utf-8")
    tables = soup.findAll("table", {"class" : "cTblListBody"})
    for table in tables:
        headers = table.find_all("td", {"class" : "cColHeaderTxt"})[1:]
        headers = [i.getText() for i in headers]
        ncols = len(headers)
        all_hrefs = table.find_all("a", href=True)
        people_elems = [i for i in all_hrefs if i["href"].startswith("/CIQDotNet/person.aspx")]
        people = [i.getText() for i in people_elems]
        titles = [i.findNext("td").getText() for i in people_elems]
        comp_elems = table.find_all("div", {"class" : "cTblsummaryRow"})
        
        ipdb.set_trace()

        
    
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
        self.driver.find_element_by_id("myCompanyExcelReport").click()
        return self.driver.page_source
        
    
    def main(self):
        try:
            self.open_browser()
            self.do_login()
            data = self.get_comp_data()
            ipdb.set_trace()
            print(data)
            return data
        except Exception:
            traceback.print_exc()
        finally:
            self.driver.quit()

def main():
#    sc = Scraper()
#    data = sc.main()
    data = pickle.load(open("site_data.p", "rb"))
    parse(data)

if __name__ == "__main__":
    main()
