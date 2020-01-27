import sys

def main():
    n_m = sys.stdin.readline()[:-1]
    while(n_m != ""):
        n, m = n_m.split()
        n, m = int(n), int(m)
        data = {}
        elements = sys.stdin.readline()[:-1].split()
        for ind, ele in enumerate(elements):
            if ele not in data:
                data[ele] = []
            data[ele].append(ind)
        for _ in range(m):
            k,v = sys.stdin.readline()[:-1].split()
            k = int(k)
            if k <= len(data[v]):
                print(data[v][k-1]+1)
            else:
                print('0')
            
        n_m = sys.stdin.readline()[:-1]
    

main()