import sys


def main():
    input_number = int(sys.stdin.readline()[:-1])
    while(input_number):
        one_indcies = []
        for i in range(0,32):
            if (1<<i) & input_number:
                one_indcies.append(i)
        a = 0
        b = 0
        for i in range(len(one_indcies)):
            if i % 2 == 0:
                a = a | (1 << one_indcies[i])
            else:
                b = b | (1 << one_indcies[i])
        print(a,b)
        input_number = int(sys.stdin.readline()[:-1])
main()