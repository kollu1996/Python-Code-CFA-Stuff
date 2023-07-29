import cfscrape
from bs4 import BeautifulSoup as bs
import re
import lxml
import pandas as pd
import time
import numpy as np
import xlrd
from pandas import ExcelWriter
from multiprocessing import Pool
from pandas import ExcelWriter
from multiprocessing import Pool
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime as dt
from datetime import datetime
from dateutil.parser import parse
import calendar
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import urllib.parse
import json
import urllib.request
import urllib3
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

# http://www.basnews.com/en/bash/76 ---------->   Kurdistan
# http://www.basnews.com/en/bash/77 ----------->  Iraq
# http://www.basnews.com/en/bash/78 ------------> Middle East


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(50)
        self.driver.maximize_window()

    def test_Mahsum_Pass(self):
        maincontent = []
        source = []
        datetime = []
        urls = []
        heading = []
        s = 0
        allurl = ["http://www.basnews.com/en/bash/76", "http://www.basnews.com/en/bash/77", "http://www.basnews.com/en/bash/78"]
        for t in range(0, len(allurl)):
            list2 = []
            suburlist = []
            z = 0
            url = allurl[t]
            if t == 0:
                s = 2
            elif t == 1:
                s = 1
            else:
                s = 1
            while True:
                self.driver.get(url)
                list2.append(url)
                sleep(5)
                if z == s:
                    break
                k = self.driver.execute_script("return document.body.innerHTML")
                page = bs(k, 'lxml')
                print(page.prettify())
                alllinks = page.find('span',attrs = {'class': 'pesh'})
                item = alllinks.find('a')
                m = "http://www.basnews.com" + item.get('href')
                print(m)
                url = m
                z+=1
            print(list2)

            for p in range(0, len(list2)):
                self.driver.get(list2[p])
                k = self.driver.execute_script("return document.body.innerHTML")
                page = bs(k, 'lxml')
                sublist = (page.find_all('div', attrs={'class': 'brga1'}))
                for i in range(0, len(sublist)):
                    links1 = sublist[i].find('a')
                    suburlist.append(("http://www.basnews.com" + links1.get('href')))
            print("The suburl is: ", suburlist)

            for q in range(0, len(suburlist)):
                self.driver.get(suburlist[q])
                k = self.driver.execute_script("return document.body.innerHTML")
                subpage = bs(k, 'lxml')
                datetime1 = subpage.find('span', attrs={'class': 'katzhmer'})
                maincontent1 = subpage.find('div', attrs={'class': 'full'})
                heading1 = subpage.find('div', attrs= {'class': 'tanisht'})
                heading2 = heading1.find('h2')
                datetime.append(datetime1.text.strip())
                source.append("Bas News")
                maincontent.append(maincontent1.text)
                heading.append(heading2.text)
                urls.append(suburlist[q])


        print(len(urls))
        print(len(heading))
        print(len(datetime))
        print(len(maincontent))
        print(len(source))
        df = pd.DataFrame({'Date_Published': datetime, 'Source_Name': source, 'Article_Text': maincontent, 'Title': heading, 'URL': urls})
        print(df)
        writer = ExcelWriter('Bas News english july 20th - july 27th.xlsx')
        df.to_excel(writer)
        writer.save()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
