import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# input your page to parse
url = input('Enter location: ')
if len(url) < 1:
    #use the default page if user did not enter any.
    url=' http://py4e-data.dr-chuck.net/comments_42.xml'

#get URL
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree=ET.fromstring(data)
resultsSum = 0

# find all the comments
results=tree.findall('comments/comment')
print('type of results:',type(results))

#Count the items
print('Count:',len(results))

#Sum all the count from the XML
for result in results:
    count=int(result.find('count').text)
    #print('current count=',count)
    resultsSum = resultsSum+count
print('Sum:',resultsSum)
