import sys
n = int(sys.stdin.readline())
numbers = sorted([int(ele) for ele in sys.stdin.readline()[:-1].split()])
for i,ele in enumerate(numbers):
    print(int(ele),end=' ')
