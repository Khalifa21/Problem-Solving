import sys
n = int(sys.stdin.readline()[:-1])
count = 0
for _ in range(n):
    num1, num2, num3 = sys.stdin.readline()[:-1].split()
    num1, num2, num3 = int(num1), int(num2), int(num3)
    if num1+num2+num3 >= 2:
        count +=1 
print(count)
