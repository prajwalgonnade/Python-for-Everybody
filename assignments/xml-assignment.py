import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter - ')
dataurl = urllib.urlopen(url).read()

tree = ET.fromstring(dataurl)
comment = tree.findall('.//comment')

all_counts = list()
for item in comment:
   all_counts.append(item.find('count').text)
#print all_counts

for i in range(len(all_counts)):
    all_counts[i] = int(all_counts[i])
    
#print(all_counts)
print sum(all_counts)