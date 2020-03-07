import sys
n = int(sys.stdin.readline()[:-1])
magnet = sys.stdin.readline()[:-1]
last = magnet[-1]
output = 1
for i in range(n-1):
    magnet = sys.stdin.readline()[:-1]
    if magnet[0] == last:
        output +=1
        last = magnet[-1]
print(output)