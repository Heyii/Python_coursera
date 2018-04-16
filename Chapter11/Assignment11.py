import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle=open(name)
#countline=0
sumtxt=0
for line in handle:
    countline=countline+1
    print(countline)
    d=re.findall('[0-9]+',line)
#    print(d)
    for num in d:
        intd=int(num)
        sumtxt=sumtxt+intd
print(sumtxt)
