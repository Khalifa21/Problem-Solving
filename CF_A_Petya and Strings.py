import sys
first = sys.stdin.readline()[:-1].lower()
second = sys.stdin.readline()[:-1].lower()
length = len(first)
output = 0
for i in range(length):
    if first[i] < second[i]:
        output = -1
        break
    elif first[i] > second[i]:
        output = 1
        break
print(output)