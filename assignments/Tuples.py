name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
counts = dict()
hour = list()
sortCount = dict()


for line in handle:
    line = line.rstrip()
    if not 'From ' in line: continue
    new = line.split()
    time = new[5]
    hours = time.split(":")
    hour.append(hours[0])
#print hour

for count in hour:
    counts[count] = counts.get(count,0) + 1
    
#print counts

for k, v in sorted(counts.items()):
    print k,v