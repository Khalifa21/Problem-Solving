import sys
name = sys.stdin.readline()[:-1]
name = 'a'+name

output = 0
for i in range(0,len(name)-1):
    suggested = abs(ord(name[i])-ord(name[i+1]))
    if suggested > 13:
        output += (26 - suggested)
    else:
        output += suggested
print(output)