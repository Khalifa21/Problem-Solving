import sys
limak,bob = sys.stdin.readline()[:-1].split()
limak,bob = int(limak),int(bob)
count = 0
while (limak<=bob):
    limak *= 3
    bob *=2
    count +=1 
print(count)