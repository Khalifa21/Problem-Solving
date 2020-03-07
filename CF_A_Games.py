import sys
n = int(sys.stdin.readline()[:-1])
teams = []
for i in range(n):
    team = [int(ele) for ele in sys.stdin.readline()[:-1].split()]
    teams.append(team)
output = 0
for i in range(0, len(teams)):
    for j in range(0,len(teams)):
        if teams[i][0] == teams[j][1]:
            output +=1
print(output)