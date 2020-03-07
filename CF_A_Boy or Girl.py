import sys
chars = sys.stdin.readline()[:-1]
chars_set = set(chars)
if len(chars_set)%2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")