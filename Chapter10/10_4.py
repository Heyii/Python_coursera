name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith('From '):
        TextPieces=line.split()
        stime=TextPieces[5]
        shhmmss=stime.split(':')
        shour=shhmmss[0]
        counts[shour]=counts.get(shour,0)+1
#print(counts)

# sort by hours
lst=list()
#for h,t in list(counts.items()):
#    lst.append((h,t))

lst=list(counts.items())
lst.sort()
for l in lst:
    print(l[0],l[1])

#print(lst)
