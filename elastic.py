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

scraper = cfscrape.create_scraper()
page = bs(scraper.get('https://www.iraqinews.com/iraq-war/two-iraqi-farmers-killed-in-bomb-blast-in-nineveh/').content, 'lxml')
list1 = (page.body.findAll(text= re.compile(('sAiD'), re.I)))
for item in list1:
    print(item)
