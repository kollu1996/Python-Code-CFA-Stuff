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
from selenium import webdriver
from ahocorapy.keywordtree import KeywordTree
import math

class mydictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


df = pd.read_excel('/Users/sreenikhilkollu/PycharmProjects/scrapy/venv/sohr news4.xlsx')
list1 = df['maincontent']
list3 = df['url']
list2 = []
for i in range(0, len(list1)):
    if list1[i] == '\n':
        print(i)
        list2.append(list3[i])

print(len(list2))
print(list2)

linksall = list2
heading = []
datetime =[]
source = []
main = []
url = []
megalist = []
print(linksall)
k = 0

for i in range(0, len(linksall)):
    print(linksall[i])
    s = linksall[i]
    dictobj = mydictionary()
    whole = ""
    scraper = cfscrape.create_scraper(delay = 6)
    page = bs(scraper.get(linksall[i]).content, 'lxml')
    heading = page.find('h1', attrs={'class': 'post-title entry-title'})
    datetime1 = page.find('span', attrs={'class': 'date meta-item'})
    datetime2 = datetime1.find('span', attrs={'class': ''})
    source1 = page.find('div', attrs={'class': 'image-logo', 'id': 'logo'})
    source2 = source1.find('a')
    maincontent1 = page.find('div', attrs={'class':'entry-content entry clearfix'})

    dictobj.add('datetime',(datetime2.text).strip())
    dictobj.add('source', source2.get('title'))
    dictobj.add('maincontent', maincontent1.text)
    dictobj.add('headings', heading.text)
    dictobj.add('url', s)
    megalist.append(dictobj)
    k+=1
    print(k)


df = pd.DataFrame(megalist)
print(df)


writer = ExcelWriter('sohr news4 corrected file.xlsx')
df.to_excel(writer)
writer.save()