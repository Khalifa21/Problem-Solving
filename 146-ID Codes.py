import sys


def replacement_fix(word,mn_ind):
    highest_diff = 1000
    replacement_ind = -1
    for i in range(mn_ind,len(word)):
        diff = ord(word[i]) - ord(word[mn_ind])
        if diff < highest_diff and diff > 0:
            replacement_ind = i

    word = list(word)
    word[mn_ind], word[replacement_ind] = word[replacement_ind], word[mn_ind]
    pre = word[0:mn_ind+1]
    post = sorted(word[mn_ind+1:])
    output = []
    output.extend(pre)
    output.extend(post)
    return output


def main():
    input_word = sys.stdin.readline()[:-1]
    while(input_word != "#"):
        size = len(input_word)
        mn_ind = size - 1
        mx_ind = size - 1
        change_ind = -1
        for i in range(size-1, 0, -1):
            if input_word[i-1] < input_word[i]:
                change_ind = i-1
                break
        if change_ind == -1:
            print("No Successor")
        else:
            input_word = replacement_fix(input_word,change_ind)
            input_word = "".join(input_word)
            print(input_word)
        input_word = sys.stdin.readline()[:-1]

main()