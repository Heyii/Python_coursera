import json
import urllib.request,urllib.parse,urllib.error

# input the url
url=input('Enter location:')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_42.json'
#Print input url
print('Retrieving:',url)

#connect with the url
uh=urllib.request.urlopen(url)


#load url contents
contents=uh.read().decode()
print('Retrieved',len(contents),'characters')
#check the contents of the json
#print(contents)

#load json, converting it to a dict type data
try:
    js=json.loads(contents)
except:
    js=None

count=0
sums=0
#check the type of js
#print('type',type(js))
#print(json.dumps(js,indent=4))
#count the number of students
for c in js['comments']:
    #print(c['count'])
    count=count+1
    sums=sums+c['count']
print('Count:',count)
print('Sum:',sums)
