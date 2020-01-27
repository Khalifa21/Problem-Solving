import sys

def main():
    n, m = sys.stdin.readline()[:-1].split()
    n, m = int(n), int(m)
    while not (n == 0  and m == 0):
        cds = {}
        for j in range(n):
            input_cd = sys.stdin.readline()[:-1]
            if cds.get(input_cd):
                cds[input_cd] += 1
            else:
                cds[input_cd] = 1
        for j in range(m):
            input_cd = sys.stdin.readline()[:-1]
            if cds.get(input_cd):
                cds[input_cd] += 1
            else:
                cds[input_cd] = 1
        output = 0
        for cd in cds.keys():
            if cds[cd] > 1:
                output += 1
        print(output)
        n, m = sys.stdin.readline()[:-1].split()
        n, m = int(n), int(m)

main()