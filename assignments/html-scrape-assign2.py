import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

for i in range(7):
    html = urllib.urlopen(url).read()
   # print i
   # print html
    soup = BeautifulSoup(html)
    x = list()
    y = list()
    tags = soup('a')
    for tag in tags:

      #  print tag.get('href', None)
       # print tag.contents[0]
        x.append(tag.get('href', None))
        y.append(tag.contents[0])
        
    #print "-----------------------------------------------------------------"
    #print x[2]
    url = x[17]

    #print "-----------------------------------------------------------------"


print y[17]