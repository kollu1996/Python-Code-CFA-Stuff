import csv
import json
import re
import sys
from time import sleep
from collections import OrderedDict
from collections import defaultdict
import requests


'''
sys.argv[0] # Graduate
sys.argv[1] # Education
sys.argv[2] # Career
'''

def create_json_file():

    filepath1 = "/Users/sreenikhilkollu/PycharmProjects/scrapy/AI_ML Companies/Company_AI_ML updated/company_sheet.csv"
    filepath2 = "/Users/sreenikhilkollu/PycharmProjects/scrapy/AI_ML Companies/Company_AI_ML updated/alias_sheet_2.csv"
    filepath3 = "/Users/sreenikhilkollu/PycharmProjects/scrapy/AI_ML Companies/Company_AI_ML updated/parent_sheet.csv"
    filepath4 = "/Users/sreenikhilkollu/PycharmProjects/scrapy/AI_ML Companies/Company_AI_ML updated/market_sheet.csv"


    csvfile1 = open(filepath1, encoding="latin1", errors="ignore")

    csvReader1 = csv.DictReader(csvfile1)

    '''
    for csv1 in csvReader1:
        print("First file: ", csv1)
        print("\n")
    for csv2 in csvReader2:
        print("Second file: ", csv2)
        print("\n")
    for csv3 in csvReader3:
        print("Third file: ", csv3)
        print("\n")
    for csv4 in csvReader4:
        print("Fourth file: ", csv4)
        print("\n")
    '''

    output_new = []

    print("Successfully created json file")
    # merge province_state, country, city
    for csv1 in csvReader1:
        output = {}
        output1 = {}
        csvfile2 = open(filepath2, encoding="latin1", errors="ignore")
        csvReader2 = csv.DictReader(csvfile2)
        csvfile3 = open(filepath3, encoding="latin1", errors="ignore")
        csvReader3 = csv.DictReader(csvfile3)
        csvfile4 = open(filepath4, encoding="latin1", errors="ignore")
        csvReader4 = csv.DictReader(csvfile4)



        output2 = {}
        output3 = {}
        output4 = {}
        aliasList  = []
        aliasList1 = []
        aliasList2 = []

        for csv2 in csvReader2:

            if csv1['Main_ID'] == csv2['Main_ID']:

                output2['alias'] = csv2['Alias']
                output2['alias_language'] = csv2['Alias_language']
                aliasList.append(output2)
                output2 = {}


        csv1['aliases'] = aliasList


        for csv3 in csvReader3:


            if csv1['Main_ID'] == csv3['Main_ID']:
                output3['parent_name'] = csv3['Parent_name']
                output3['parent_acquisition'] = csv3['Parent_acquisition']

                aliasList1.append(output3)
                output3 = {}

        csv1['parent'] = aliasList1


        for csv4 in csvReader4:


            if csv1['Main_ID'] == csv4['Main_ID']:
                output4['ticker'] = csv4['Ticker']
                output4['exchange'] = csv4['Exchange']

                aliasList2.append(output4)
                output4 = {}

        csv1['market'] = aliasList2

        csv1.pop('Main_ID')
        output1['crunchbase_url'] = csv1['crunchbase_url']
        output1['crunchbase_uuid'] = csv1['crunchbase_uuid']
        csv1['crunchbase'] = output1
        csv1.pop('crunchbase_url')
        csv1.pop('crunchbase_uuid')

        output['country'] = csv1['Country']
        output['province_state'] = csv1['Province_State']
        output['city'] = csv1['City']

        csv1['location'] = output
        csv1.pop('Country')
        csv1.pop('Province_State')
        csv1.pop('City')

        if csv1['grid']:
            print("Grid is not empty")
        else:
            # Write all the logic here
            regex = ""
            for alpha in csv1['Name']:
                if alpha.isspace():
                    regex = regex + "\s"
                elif alpha.isalpha():
                    regex = regex + "[" + alpha.upper() + alpha.lower() + "]"
                else:
                    regex = regex + "[" + alpha + "]"
            finalValue =  "\\" + "b" + regex + "\\" +  "b"
            csv1['no_grid'] = finalValue

        # We shall do the magic
        csv1['name'] = csv1['Name']
        csv1['website'] = csv1['Website']
        csv1.pop('Name')
        csv1.pop('Website')



        #print("The location is: ", csv1['location'])

        # Here we have to write logic to keep every thing ordered
        key_order = ["name", "location", "website", "aliases", "parent", "permid", "market", "crunchbase", "grid", "no_grid"]
        result = {}
        ordered = OrderedDict((key, csv1.get(key)) for key in key_order)

        output_new.append(ordered)  # This line is very critical
        print(output_new)



    output_new1 = json.dumps(output_new, indent=4, separators=None, ensure_ascii=False)
    with open("AI-ML Companies One.json", 'w', encoding="latin1") as jsonfile:
         jsonfile.write(output_new1)

'''
    #Now it makes sense

    for csv1 in csvReader1:
        csv1['Education'] = []
        csv1['Career'] = []
        result = csv1['Subject'].split(',')
        result1 = csv1['Committee'].split(',')
        csv1['Subject'] = []
        csv1['Committee'] = []
        newlist = []
        newlist1 = []
        newlist2 = []
        newlist3 = []


        csvfile2.seek(0)        #Setting to starting point
        csvfile3.seek(0)

        for csv2 in csvReader2:
            result3 = csv2['Location'].split(',')
            for t in range(0, len(result3)):
                newlist3.append(result3[t].strip())
            csv2['Location'] = []
            csv2['Location'] = newlist3

            csv2['Location'] = []
            if csv2['GITID'] == csv1['GITID']:
                 csv2.pop("GITID")
                 csv2['Location'] = result3

                 pdes = re.sub('\s+', ' ', csv2['Description'])
                 qdes = pdes.strip()
                 qdes1 = qdes.replace('"', "'")
                 csv2['Description'] = qdes1

                 csv1['Education'].append(csv2)

                 p  = re.sub('\s+', ' ', csv1['Data_Quality_Notes'])
                 q = p.strip()
                 q1 = q.replace('"', "'")
                 csv1['Data_Quality_Notes'] = q1


                 pabs = re.sub('\s+', ' ', csv1['Abstract'])
                 qabs = pabs.strip()
                 qabs1 = qabs.replace('"', "'")
                 csv1['Abstract'] = qabs1

        psub_mul = re.sub('\s+', ' ', csv1['Subjects_Multiple'])
        qsub_mul = psub_mul.strip()
        csv1['Subjects_Multiple'] = qsub_mul


        for h in range(0, len(result)):
            psub = re.sub('\s+', ' ', result[h])
            qsub = psub.strip()
            newlist1.append(qsub)
        csv1['Subject'] = newlist1


        for h1 in range(0, len(result1)):
            newlist.append(result1[h1].strip())
        csv1['Committee'] = newlist

        for csv3 in csvReader3:
            result4 = csv3['Location'].split(',')
            for t in range(0, len(result4)):
                newlist2.append(result4[t].strip())
            csv3['Location'] = []
            csv3['Location'] = newlist2
            newlist2 = []

            if csv3['GITID'] == csv1['GITID']:
                csv3.pop("GITID")

                pemp = re.sub('\s+', ' ', csv3['Employer'])
                qemp = pemp.strip()
                qemp1 = qemp.replace('"', "'")
                csv3['Employer'] = qemp1

                pdes = re.sub('\s+', ' ', csv3['Description'])
                pdes2 = pdes.strip()
                pdes3 = pdes2.replace('"', "'")
                csv3['Description'] = pdes3

                csv1['Career'].append(csv3)


        csv1.pop('GITID')
        output_new.append(csv1)
        #Aoutput[record_id] = csv1
        #record_id+=1


    output_new1 = json.dumps(output_new, indent=4, separators=None, ensure_ascii=False)
    output_new2 = re.sub(r"\\", '', output_new1)

    with open("jsonoutput1.json", 'w', encoding = "latin1") as jsonfile:
        jsonfile.write(output_new2)

    jsonfile.close()
'''
'''
def verify_output():
    try:
        with open("jsonoutput.json", "r", encoding="latin1") as produced_json:
            data = json.load(produced_json)
            print("I am in the try block")
            print(data)
            # We can check for all problems here
            webhool_url = 'https://hooks.slack.com/services/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'
            slack_msg = {'text': 'Everything is fine, file created'}
            requests.post(webhool_url, data=json.dumps(slack_msg))

    except:
        webhool_url = 'https://hooks.slack.com/services/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'
        slack_msg = {'text': 'File not created'}
        requests.post(webhool_url, data=json.dumps(slack_msg))
        print("File not created")
'''



if __name__ == "__main__":
    print("Creating a JSON File")
    create_json_file()
    sleep(5)
    print("Created json file succcessfully")




'''
json_output = json.dumps(output, indent= 4, separators=None, ensure_ascii=False)
print(json_output[0])
print(json_output[-1])
newstr = json_output[1:-1]
print(newstr)
with open("newjson22.json", 'w') as jsonfile:
    jsonfile.write(newstr)
'''


'''
json_output = json.dumps(output, indent= 4, separators=None, ensure_ascii=False)
newstr = json_output[1:-1]
print(type(newstr))
data = json.loads(json_output)
print(type(data))

d1 = {"('Hello',)": 6, "('Hi',)": 5}
s1 = json.dumps(d1)
d2 = json.loads(s1)
print(type(d2))
'''

'''
with open("/Users/sreenikhilkollu/PycharmProjects/scrapy/newjson18.json", 'r') as json_file:
    print(json_file)
    data = json.loads(json_file)
    print(type(data))
'''



'''
with open("newjson17.json", 'w') as jsonfile:
    jsonfile.write(json.dumps(output, indent= 4, separators=None, ensure_ascii=False))

jsonfile.close()



output_new = json.dumps(output, indent=4, ensure_ascii=False)
output2 = re.sub(r"\\", '', output_new)
print(output2)

with open("newjson19.json", 'w') as jsonfile:
    jsonfile.write(output2)
'''


'''
output_new1 = json.dumps(output, indent=4, separators=None, ensure_ascii=False)


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        print("I am flattening")
        out[name[:-1]] = x.replace('\n', '')

    flatten(y)
    return out

flat = flatten_json(output_new1)

df = pd.DataFrame(json_normalize(flat))
print(df.head())
'''


'''
json_data  = json.dumps(output, indent= 4, separators=None, ensure_ascii=False)
out = {}
out['value'] = json_data
normalized_data  = json_normalize(out)
print(normalized_data)

'''

'''

value = json.loads(json.dumps(output, indent=4, separators=None, ensure_ascii=False))
print(type(value))
print(value)
serialized_value = json.dumps(value)
print(type(serialized_value))
print(serialized_value)

'''



#sample = json_normalize(value)
#print(sample)
#df = pd.DataFrame(output)
#print(df)
#path = 'out.json'
#df.to_json(path, orient='records')


'''
token = "xoxb-3361732215-1155267272836-JVF1p0qQ1QaO0IXfDUBwyABY"
slack = Slacker(token)
slack.chat.post_message('# c-random', 'Hi', as_user=True)
'''

'''
def verify_output():
    try:
         webhool_url = 'https://hooks.slack.com/services/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'
         slack_msg = {'text': 'Everything is fine, published to Tableau Server'}
         requests.post(webhool_url, data=json.dumps(slack_msg))

    except:
        webhool_url = 'https://hooks.slack.com/services/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'
        slack_msg = {'text': 'File to publish to Tableau Server'}
        requests.post(webhool_url, data=json.dumps(slack_msg))
        print("File not created")




if __name__ == "__main__":
    print("Verifying output ...")
    verify_output()
'''

'''
               if bool():
                   map_alias.update(output2)
               else:
                   map_alias.add(csv1['id'], output2)
               aliasList.append(output2)
               '''