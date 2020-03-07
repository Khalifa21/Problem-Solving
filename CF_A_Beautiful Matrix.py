import sys
one_row = -1
one_col = -1
for i in range(5):
    row = sys.stdin.readline()[:-1].split()
    for j in range(5):
        if row[j] == '1':
            one_row = i
            one_col = j
            break
print(abs(one_row - 2)+abs(one_col - 2))
