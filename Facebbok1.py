from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import ExcelWriter
import unittest
from selenium import webdriver
import os


class TestClass(unittest.TestCase):
    # Before executing the test case
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(50)   # set the load time so that if page takes time to load the test case is not terminated
        self.driver.maximize_window()
    # Test case

    def test_Facebook_Pages(self):
            url1 = []
            # This path is specific to the computer.
            # file:///Users/sreenikhilkollu/PycharmProjects/scrapy
            filename = "your_messages.html"
            self.driver.get("file://" + os.path.realpath(filename))
            k = self.driver.execute_script("return document.body.innerHTML")
            page = bs(k, 'lxml')

            m = page.find_all('div', attrs={'class': '_2lek'})
            for p in range(0, len(m)):
                n = m[p].find('a').get('href')
                # This path is to get all individual files.
                url1.append("file://" + os.path.realpath(n))
            name = []
            message = []
            time = []
            print(url1)
            for h in range(0, len(url1)):
                print("I am in magic loop")
                self.driver.get(url1[h])
                s = self.driver.execute_script("return document.body.innerHTML")
                subpage = bs(s, 'lxml')
                section = subpage.find_all('div', {'class': 'pam _3-95 _2pi0 _2lej uiBoxWhite noborder'})
                for s1 in range(0, len(section)):
                    name1 = section[s1].find('div', {'class': '_3-96 _2pio _2lek _2lel'})
                    if name1 is not None:
                        name.append(name1.text)
                    else:
                        name.append("")
                    message1 = section[s1].find('div', {'class': '_3-96 _2let'})
                    if message1 is not None:
                        message.append(message1.text)
                    else:
                         message.append("")
                    time1 = section[s1].find('div', {'class': '_3-94 _2lem'})
                    if time1 is not None:
                        time.append(time1.text)
                    else:
                        time.append("")
            print(name)
            print(message)
            print(time)
            df = pd.DataFrame({'Names': name, 'Messages': message, 'Time': time})
            print(df)
            writer = ExcelWriter('Facebook 4.xlsx')
            df.to_excel(writer)
            writer.save()

    # After executing the test case
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
