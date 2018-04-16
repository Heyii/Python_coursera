counts=dict()
print('Enter a line of text:')
line=input('')
words=line.split()
print('Words:',words)
print('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
    ##Dictionaries have a method called get that
    ##takes a key and a default value. If the key
    #appears in the dictionary, get returns the
    #corresponding value; otherwise it returns
    #the default value.
print('Counts:',counts)
