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

#------------------------ For Bas News ---------------------------------

df = pd.read_excel("/Users/sreenikhilkollu/PycharmProjects/scrapy/Bas News english oct 27th  - nov 3rd.xlsx")
list1 = df['datetime']
list4 = []
list5 = []


basPrgm = re.compile(r'(0[1-9]|[12]\d|3[01])\/[01]\d\/20\d\d[\s\S]*')
hadthPrgm = re.compile(r'(0[1-9]|[12]\d|3[01])\-(09|10)\-2019')
hadthPrgm1 = re.compile(r'2019\-(0[1-9]|[12]\d|3[01])\-(09|10)')
sumarPrgm = re.compile(r'2019\-09\-(0[1-9]|[12]\d|3[01])[\s\S]*')


'''
#----------------- FOR Al SUMARIA NEWS ---------------------------------

for i in range(0, len(list1)):
    list5.append(list1[i])

print(len(list5))

z = 0
for i in range(0, len(list5)):
    m = list5[i]
    if re.match(sumarPrgm, str(m)):
        z+=1
        print("I did a great job")
        m = m.replace('|', '-')
        list3 = m.split('-')
        list3[0], list3[1] = list3[1], list3[0]
        list3[1], list3[2] = list3[2], list3[1]
        print(list3)
        k = ""
        for i in range(0, len(list3) - 1):
            k = k + list3[i].strip() + '/'
            i += 1
        print(k[:-1])
        list4.append(k[:-1])
    else:
        list4.append(m)

print(list4)
df['New_Date'] = list4
print(df)
writer = ExcelWriter("Bas News english oct 27th  - nov 3rd.xlsx")
df.to_excel(writer)
writer.save()
'''

#------------------- FOR BAS NEWS ---------------------------------

for i in range(0, len(list1)):
    list5.append(list1[i])

print(len(list5))

for i in range(0, len(list5)):
    m = list5[i]
    if re.match(basPrgm, str(m)):
        print("I did a great job")
        print(m)
        m = m.replace('-', '/')
        list2 = m.split('/')
        list2[0], list2[1] = list2[1], list2[0]
        list3 = []
        print(list2)
        k = ""
        for r in range(0, len(list2)-1):
            k = k + list2[r] + '/'
        print(k)
        list4.append(k[:-1])
    else:
        print("I did not match due to follwing reasons: ", m)
        list4.append(m)

print(list4)
df['New_Date'] = list4
print(df)
writer = ExcelWriter("Bas News english oct 27th  - nov 3rd.xlsx")
df.to_excel(writer)
writer.save()


#-------------------- FOR AL HADATH ---------------------------
'''
for i in range(0, len(list1)):
    list5.append(list1[i])
z=0
x=0
print(len(list5))
for i in range(0, len(list5)):
    m = list5[i]
    if re.match(hadthPrgm, str(m)):
        z+=1
        print("I did a great job")
        list2 = m.split('-')
        list2[0], list2[1] = list2[1], list2[0]
        k = ""
        for r in range(0, len(list2)):
            k = k + list2[r] + '/'
        list4.append(k[:-1])

    if re.match(hadthPrgm1, str(m)):
        x+=1
        print("I did another great job")
        list3 = m.split('-')
        list3[0], list3[2] = list3[2], list3[0]
        q = ""
        for n in range(0, len(list3)):
            q = q + list3[n] + '/'
        list4.append(q[:-1])

print(list4)

print(z)
print(x)
df['New_Date'] = list4
print(df)
writer = ExcelWriter("Al Hadath sept and oct without duplicates.xlsx")
df.to_excel(writer)
writer.save()
'''