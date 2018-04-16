#Calling a JSON API
#In this assignment you will write a Python program somewhat similar
# to http://www.py4e.com/code3/geojson.py. The program will prompt
# for a location, contact a web service and retrieve JSON for the web
#service and parse that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as
#within Google Maps.

import json
import urllib.request,urllib.parse,urllib.error

serviceurl='http://py4e-data.dr-chuck.net/geojson?'

#Get the name of the location
address=input('Enter address:')
if len(address)<1:
    address = 'South Federal University'

print(urllib.parse.urlencode({'address':address}))

url=serviceurl+urllib.parse.urlencode({'address':address})
#print('Retrieving',url)
print('Retrieving',url)

#use url handle to connect the url
uh=urllib.request.urlopen(url)

#get data from the url and decode it into UTF-8
data=uh.read().decode()

#print the length of data
print('Retrieved',len(data),'characters')

#load the json from the data
try:
    js=json.loads(data)
except:
    js=None

#print(json.dumps(js,indent=4))

#find the id
placeid=js['results'][0]["place_id"]
print("Place ID",placeid)
