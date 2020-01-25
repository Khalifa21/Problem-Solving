import sys
import re

def main():
    test_cases = int(sys.stdin.readline()[:-1])
    printed = 0
    for k in range(test_cases):
        if k == 0:
            sys.stdin.readline()
        words_dict = {}
        input_word = sys.stdin.readline()
        input_word = re.sub("\n|\t|\r|\r\n", "", input_word)
        while len(input_word) > 1:
            sorted_input = ''.join(sorted(''.join(input_word.split())))
            if sorted_input not in words_dict.keys():
                words_dict[sorted_input] = [input_word]
            else:
                words_dict[sorted_input].append(input_word)
            input_word = sys.stdin.readline()
            input_word = re.sub("\n|\t|\r|\r\n", "", input_word)

        for values in words_dict.values():
            values.sort()
        tuples_list = []
        for values in words_dict.values():
            for i in range(len(values) - 1):
                for j in range(i + 1, len(values)):
                    tuples_list.append((values[i], values[j]))

        tuples_list = sorted(tuples_list)

        for tuples in tuples_list:
            print(tuples[0]+" = "+tuples[1])

        if k!= test_cases-1:
            print()
main()