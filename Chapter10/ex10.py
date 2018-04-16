name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith('From '):
        texts=line.split()
#        print(texts)
        sender=texts[1]
        counts[sender]=counts.get(sender,0)+1
print(counts)
Senderlist=list()
for s,v in list(counts.items()):
    Senderlist.append((v,s))
Senderlist.sort(reverse=True)
for v,s in Senderlist[:10]:
    print(v,s)
