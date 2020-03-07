import sys

n,h = sys.stdin.readline()[:-1].split()
n,h = int(n),int(h)
heights = sys.stdin.readline()[:-1].split()
output = 0
for i in range(n):
    if int(heights[i]) > h:
        output += 2
    else:
        output += 1
print(output)