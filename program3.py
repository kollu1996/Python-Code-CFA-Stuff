import sys

my_dict={}
#reading from a text file
print("reading from a text file")
myFile=open("Book.txt", "r",encoding = 'utf-8')
data=myFile.read()
print("How many lines in a file?")
#How many lines in a file?
data = open('Book.txt',encoding = 'utf-8')
count = 0
for line in data:
     count = count + 1
print('Line Count:', count)
key='Line Count:'
value=count
my_dict[key]=value
#How many "." in a file?

myFile = open("Book.txt", "r",encoding = 'utf-8')
data = myFile.read().replace('\n', '')
count = 0
for i in data: 
    if i == '.': 
        count = count + 1  
print(count)
                           
key='"." Count:'
value=count
my_dict[key]=value

#data=open('Book.txt')
#for line in data:
 #   print(line)#Print all the lines in a file?

#what are the first and last words?

str = open("Book.txt", "rt", encoding = 'utf-8')
res = str.read()
file = res.split()
fir = file[0]
fin = file[-1]
print(fir, fin)
key='First word'
value=file[0]
my_dict[key]=value
key='Last word'
value=file[-1]
my_dict[key]=value
print(my_dict)

sys.stdout = open('file3.txt', 'w')
print(my_dict)