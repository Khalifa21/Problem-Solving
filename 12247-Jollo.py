def get_higher_than(element,numbers):
    output = element +1
    while output in numbers:
        output += 1
        if output > 52:
            return -1
    return output


def play(princess, prince):
    numbers = []
    numbers.extend(princess)
    numbers.extend(prince)
    prince_score = 0
    princess_score = 0
    for element in prince:
        if max(princess) < element:
            mn = min(princess)
            princess.remove(mn)
            prince_score += 1
        else:
            for i in range(len(princess)):
                if princess[i] > element:
                    del princess[i]
                    princess_score += 1
                    break
    if princess_score == 2:
        return -1
    elif prince_score == 2:
        return get_higher_than(0, numbers)
    else:
        return get_higher_than(princess[0],numbers)


def main():
    while(True):
        numbers_str = input()
        numbers = numbers_str.split()
        if numbers[0] == '0' and numbers[1] == '0':
            break
        princess = sorted([int(e) for e in numbers[0:3]])
        # prince_asc = sorted([int(e) for e in numbers[3:]])
        prince_desc = sorted([int(e) for e in numbers[3:]],reverse=True)
        # print(max(play(princess[:], prince_asc), play(princess[:], prince_desc)))
        print(play(princess[:], prince_desc))
main()