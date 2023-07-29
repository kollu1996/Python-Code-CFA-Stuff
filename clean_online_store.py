from bs4 import BeautifulSoup as bs
import re
import lxml
import pandas as pd
import time
import numpy as np
import xlrd
from pandas import ExcelWriter

'''
df = pd.read_excel('/Users/sreenikhilkollu/PycharmProjects/scrapy/Online Retail.xlsx')
list1 = df['Description']
z = 0
for i in range(0, len(list1)):
    if type(list1[i]) == float:
        print(type(list1[i]))
        list1[i] = "DUMMY PRODUCT"
        z += 1
        print(z)
        print(list1[i+1])
df['Description'] = list1
print(z)

writer = ExcelWriter('Online Retail.xlsx')
df.to_excel(writer)
writer.save()
'''

df = pd.read_excel('/Users/sreenikhilkollu/PycharmProjects/scrapy/Online Retail.xlsx')
list1 = df['Description']
z = 0
for i in range(0, len(list1)):
    if type(list1[i]) == float:
        print("I did not understand the concept")


