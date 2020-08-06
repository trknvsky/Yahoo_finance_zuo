from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv_zuo import *
import time
import os

URL = 'https://finance.yahoo.com/'


class YahooFinanceZuo:

    def parse(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir", os.getcwd())
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        driver = webdriver.Firefox(firefox_profile=fp)
        driver.get(URL)
        driver.implicitly_wait(5)
        search = driver.find_element_by_xpath('//input[@id="yfin-usr-qry"]')
        search.send_keys('zuo')
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        historical_data = driver.find_element_by_xpath('//a[@href="/quote/ZUO/history?p=ZUO"]').click()
        time_period = driver.find_element_by_xpath('//span[@class="C($linkColor) Fz(14px)"]').click()
        button = driver.find_element_by_xpath('//button[@data-value="MAX"]').click()
        download_button = driver.find_element_by_xpath('//a[@class="Fl(end) Mt(3px) Cur(p)"]').click()

        driver.quit()


def main():
    zuo = YahooFinanceZuo()
    zuo.parse()
    file = CSVFile('ZUO.csv')
    file.read()
    file.write(COMPANIES_DATA)


if __name__ == '__main__':
    main() 
