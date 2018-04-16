# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
     url= 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Input the count and position
count=input('Enter count:')
position=input('Enter position:')
count=int(count)
position=int(position)

# Retrieve all of the anchor tags

for c in range(count):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except ValueError:
        print('Error url')
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print(type(tags))
    #find the Nth position url
    if len(tags)<1:
        print('No url found')
        break
    tag=tags[position-1]
    #set the new url to open it later
    url=tag.get(('href'))
    print(url)
