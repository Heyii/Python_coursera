import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE COunts (email TEXT, count INTEGER)''')

fname = input('Enter file name:')
if (len(fname)<1):fname='mbox-short.txt'
fh = open(fname)
for line in fh:
    #print(line)
    if not line.startswith('From:'):continue
    pieces=line.split()
    print(pieces)
    #email=pieces[1]
