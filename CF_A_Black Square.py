import sys
a = [int(num) for num in sys.stdin.readline()[:-1].split()]
s = [int(num) for num in sys.stdin.readline()[:-1]]
output = 0
for ele in s:
    output += a[ele-1]

print(output)