
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
from googletrans import Translator
translator = Translator()

df = pd.read_excel()

st = "September 2, 2019 /  6:37 PM / 22 days ago"
st1 = "July 28, 2019 /  12:48 AM / 2 months ago"
st2 = "October 2, 2019 /  1:11 PM / 12 days ago"
st3 = "August 18, 2019 /  9:19 PM / a month ago"
st4 = "June 18, 2019 /  11:55 AM / 3 months ago"
st5 = "May 12, 2019 /  12:38 PM / 4 months ago"
st6 = "April 29, 2019 /  8:18 AM / 5 months ago"

list2 = [st, st1, st2, st3, st4, st5, st6]

Monthdict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

def getMonth():
    print("The month is: " + list1[0])
    print(Monthdict.get(list1[0], -1))

def getDay():
    print(list1[1].strip(','))

def getYear():
    print(list1[2])

def getAmericanDate():
    str1 = str(Monthdict.get(list1[0], -1))
    str2 = str(list1[1].strip(','))
    str3 = str(list1[2])
    str4 = str1 + "/" + str2 + "/" + str3
    print(str4)


for i in range(0, len(list2)):
    list1 = list2[i].split()
    getAmericanDate()


