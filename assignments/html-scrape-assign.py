import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

y =list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   
    y.append(tag.contents[0])
#print y

for i in range(len(y)):
    y[i] = int(y[i])
    
print(y)
print sum(y)