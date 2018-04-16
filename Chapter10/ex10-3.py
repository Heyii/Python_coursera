#Exercise 3: Write a program that reads a file and prints
#the letters in decreasing order of frequency. Your program
#should convert all the input to lower case and only count
#the letters a-z. Your program should not count spaces,
#digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see
#how letter frequency varies between languages. Compare your
#results with the tables at wikipedia.org/wiki/Letter_frequencies.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
alphabeta='abcdefghijklmnopqrstuvwxyz'
dic=dict()
for line in handle:
#line=handle.readline()
    line=line.rstrip()
    line=line.lower()
    #print(line)
    for x in line:
        #print(x)
        if x in alphabeta:
            dic[x]=dic.get(x,0)+1
            #print(dic)
diclist=list(dic.items())
diclist.sort()
for k,v in diclist:
    print(k,v)
