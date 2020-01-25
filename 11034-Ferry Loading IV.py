import sys


def main():
    test_cases = sys.stdin.readline()[:-1]
    test_cases = int(test_cases)
    for i in range(test_cases):
        l_m = sys.stdin.readline()[:-1]
        l, m = l_m.split()
        l, m = int(l)*100, int(m)
        ferry_side = 'left'
        ferry_capacity = 0
        output = 0
        left_queue = []
        right_queue = []
        for j in range(m):
            car = sys.stdin.readline()[:-1]
            car_length, car_side = car.split()
            car_length = int(car_length)
            if car_side == 'left':
                left_queue.append(car_length)
            else:
                right_queue.append(car_length)

        while len(right_queue) or len(left_queue):
            if ferry_side == 'left':
                current_queue = left_queue
            else:
                current_queue = right_queue
            while len(current_queue):
                if ferry_capacity + current_queue[0] <= l:
                    ferry_capacity += current_queue[0]
                    current_queue = current_queue[1:]
                else:
                    break
            if ferry_side == 'left':
                left_queue = current_queue
            else:
                right_queue = current_queue

            output += 1
            ferry_side = 'right' if ferry_side == 'left' else 'left'
            ferry_capacity = 0

        print(output)


main()
