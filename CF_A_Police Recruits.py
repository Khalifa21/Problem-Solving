import sys
n = int(sys.stdin.readline()[:-1])
crime_hire = [int(num) for num in sys.stdin.readline()[:-1].split()]
output = 0
officers = 0
crimes = 0
for num in crime_hire:
    if num == -1:
        crimes += 1 
        if officers == 0:
            output +=1
        else:
            officers -=1
    else:
        officers += num
print(output)