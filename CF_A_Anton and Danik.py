import sys

n = sys.stdin.readline()[:-1]
elements = sys.stdin.readline()[:-1]
anton_count = elements.count('A')
danik_count = elements.count('D')

if anton_count > danik_count:
    print("Anton")
elif danik_count > anton_count:
    print("Danik")
else:
    print("Friendship")