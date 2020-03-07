import sys
n = int(sys.stdin.readline()[:-1])
stones = sys.stdin.readline()[:-1]
ref = stones[0]
count = 0
for i in range(1,len(stones)):
    if stones[i] == ref:
        count+=1
    else:
        ref = stones[i]
print(count)