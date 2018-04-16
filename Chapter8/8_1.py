fname = input("Enter file name: ")
fhand = open(fname)
##print(fhand)
wordlist=list()
for line in fhand:
    line=line.rstrip()
    words=line.split()
    #print(line)
    #print(words)
    for word in words:
##        print(word)
##        print(words)
        if word in wordlist:
##            print(word,'is in wordslist')
            continue
##        print(word,'is not in wordslist,appended')
        wordlist.append(word)
##        print(wordlist)
wordlist.sort()
print(wordlist)
