import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text, tree.find('name').get('type'))
print('Phone:',tree.find('phone').text,tree.find('phone').get('type'))
print('Attr:', tree.find('email').get('hide'))
