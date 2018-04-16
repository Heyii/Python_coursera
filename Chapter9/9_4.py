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
MostFrequncySender=None
MostFrequncyTimer=None
for sendername,sendertime in counts.items():
    if MostFrequncyTimer is None or MostFrequncyTimer<sendertime:
#        print('sendertime',sendertime)
#        print('sendername',sendername)
#        print('MostFrenquncyTimer before',MostFrequncyTimer)
#        print('MostFrequncyTimer is None or MostFrequncyTimer<sendertime',MostFrequncyTimer is None or MostFrequncyTimer<sendertime)
        MostFrequncySender=sendername
#        print('MostFrenquncySender',MostFrequncySender)
        MostFrequncyTimer=sendertime
#        print('MostFrenquncyTimer after',MostFrequncyTimer)
print(MostFrequncySender,MostFrequncyTimer)
