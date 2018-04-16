#fname = input("Enter file name: ")
fname='mbox-short.txt'
count=0
fhand = open(fname)
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        #print(line)
        words=line.split()
        print(words[1])
        count=count+1
print('There were',count,'lines in the file with From as the first word')
