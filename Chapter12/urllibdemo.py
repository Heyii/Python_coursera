import urllib.request
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    decodeLine=line.decode().strip()
    words=decodeLine.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
