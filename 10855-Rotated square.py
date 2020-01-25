import sys


def check_match(big_square,small_square, row, col):
    n = len(small_square)
    for i,l in enumerate(range(row,row+n)):
        for j,m in enumerate(range(col,col+n)):
            if big_square[l][m] != small_square[i][j]:
                return 0
    return 1


def find_matches(big_square, small_square):
    N = len(big_square)
    n = len(small_square)
    matches = 0
    for i in range(N-n+1):
        for j in range(N-n+1):
            matches += check_match(big_square,small_square, i, j)
    return matches


def rotate(small_square):
    n = len(small_square)
    new_square = []
    for col in range(n):
        row_list = []
        for row in range(n):
            row_list.append(small_square[row][col])
        row_list.reverse()
        new_square.append(row_list)
    return new_square
def main():
    N_n = sys.stdin.readline().split()
    N,n = int(N_n[0]), int(N_n[1])
    while(N and n):
        big_square = []
        for i in range(N):
            row = [char for char in sys.stdin.readline()[:-1]]
            big_square.append(row)
        small_square = []
        for i in range(n):
            row = [char for char in sys.stdin.readline()[:-1]]
            small_square.append(row)
        match1 = find_matches(big_square, small_square)
        small_square = rotate(small_square)
        match2 = find_matches(big_square, small_square)
        small_square = rotate(small_square)
        match3 = find_matches(big_square, small_square)
        small_square = rotate(small_square)
        match4 = find_matches(big_square, small_square)
        print("{} {} {} {}".format(match1,match2,match3,match4))
        N_n = sys.stdin.readline().split()
        N, n = int(N_n[0]), int(N_n[1])
main()