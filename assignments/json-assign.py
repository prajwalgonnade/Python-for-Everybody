import json
import urllib

url = raw_input('Enter - ')
dataurl = urllib.urlopen(url).read()


info = json.loads(dataurl)
#print info
print 'User count:', len(info["comments"])

all_counts = list()
i = 0
while i < len(info["comments"]):
#    print 'Name', info["comments"][i]["name"]
    all_counts.append(info["comments"][i]["count"])
    i = i+1
    
for i in range(len(all_counts)):
    all_counts[i] = int(all_counts[i])
    
#print(all_counts)
print sum(all_counts)