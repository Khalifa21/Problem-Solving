import sys
n = sys.stdin.readline()[:-1]
numbers = [int(num) for num in sys.stdin.readline()[:-1].split()]
s_count = 0
d_count = 0
who_playes = 0
i = 0
j = len(numbers)-1
while(i<=j):
    if numbers[i] > numbers[j]:
        to_be_added = numbers[i]
        i +=1
    else:
        to_be_added = numbers[j]
        j -=1
    if who_playes == 0:
        s_count += to_be_added
        who_playes = 1
    else:
        d_count += to_be_added
        who_playes = 0
print(s_count, d_count)
