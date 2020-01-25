import sys
def main():
    numbers = sys.stdin.readline()
    while numbers != '':
        numbers = numbers.split()
        n = int(numbers[0])
        jolly_jumpers = True
        diff = []
        for i in range(1, n):
            diff.append(abs(int(numbers[i])-int(numbers[i+1])))
        diff.sort()
        for i in range(0, n-1):
            if diff[i] != i+1:
                jolly_jumpers = False
                break
        if jolly_jumpers:
            print("Jolly")
        else:
            print("Not jolly")
        numbers = sys.stdin.readline()

main()