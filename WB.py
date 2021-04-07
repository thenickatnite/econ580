#download a chrome extension json viewer
#https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh/related?hl=en-US

import json #needed for handling JSON although not intuitive
import csv #needed for writing to csv
import requests

url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2000:2001&format=json'
req = requests.get(url)
output = req.json()

# The output is a list of length two
# The second element of the main list, is a list itself of length eight, and the elements of the list are dictionaries 
output[0]['page']
output[1][0]['indicator']


for i in output[1]:
    print(i)

for i in output[1]:
    try:
        print(i['date'])
    except:
        pass

wbfile = open("wbdata.csv", 'w')
writer = csv.writer(wbfile, dialect = 'excel')
writer.writerow(['indi', 'dato', 'numero'])

for i in output[1]:
	id1 = i['country']['id']
	date1 = i['date']
	value1 = i['value']
	row = [id1, date1, value1]
	print([id1, date1, value1]) 
	writer.writerow( row )

wbfile.close()

# THIS IS A TEST