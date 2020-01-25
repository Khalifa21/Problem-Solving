import sys
from itertools import permutations


def perm(word, i, n, char_count, unique_chars):
    if i == n:
        print(word)
        return
    for char in unique_chars:
        if char_count[char] != 0:
            char_count[char] -=1
            perm(word+char,i+1,n,char_count,unique_chars)
            char_count[char] += 1

def main():
    test_cases = int(input())
    for i in range(test_cases):
        input_word = sorted(input())
        # words_list = [''.join(p) for p in permutations(input_word)]
        # print(words_list)
        # words_list = sorted(words_list)
        # print(words_list)
        # for word in words_list:
        #     print(word)
        char_count = {}
        for element in input_word:
            if char_count.get(element):
                char_count[element] += 1
            else:
                char_count[element] = 1
        unique_chars = sorted(char_count.keys(), key=str.lower)
        perm('', 0, len(input_word), char_count, unique_chars)

main()
