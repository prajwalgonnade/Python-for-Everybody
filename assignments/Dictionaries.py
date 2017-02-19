name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
emails = list()
for line in handle:
    line = line.rstrip()
    if not 'From ' in line: continue
    new = line.split()
    emails.append(new[1])

for email in emails:
    counts[email] = counts.get(email,0) + 1
    
bigword = None
bigcount = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount
