import re
import math
# import numpy as np
import sys
def create_matrix(sentence, sentence_len):
    matrix = []
    for i in range(sentence_len):
        row = []
        for j in range(sentence_len):
            row.append(sentence[i*sentence_len+j])
        matrix.append(row)
    return matrix

def check_cols_rows(matrix):
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] != matrix[j][i]:
                return -1
    for i in range(matrix_size-1,-1,-1):
        for j in range(matrix_size-1,-1,-1):
            if matrix[i][j] != matrix[j][i]:
                return -1

    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] != matrix[matrix_size-j-1][matrix_size-i-1]:
                return -1

    return matrix_size

def check_palindrome(sentence):
    sentence = ''.join(re.sub('[^A-Za-z]', ' ', sentence).split())
    sentence = [char for char in sentence]
    sentence_len = math.sqrt(len(sentence))
    if int(sentence_len) != int(math.ceil(sentence_len)):
        return -1
    sentence_len = int(sentence_len)
    # sentence_matrix = np.array(sentence)
    # sentence_matrix = sentence_matrix.reshape((sentence_len, sentence_len))
    sentence_matrix = create_matrix(sentence,sentence_len)
    # for i in range(sentence_len // 2):
    #     if (''.join(sentence_matrix[i, :]) == ''.join(sentence_matrix[:, i])) and (''.join(np.flip(sentence_matrix[sentence_len - i - 1, :])) == ''.join(np.flip(sentence_matrix[:,sentence_len - i - 1]))) and (''.join(sentence_matrix[i,:]) == ''.join(np.flip(sentence_matrix[:,sentence_len - i - 1]))):
    #         continue
    #     else:
    #         return -1
    # return sentence_len
    return check_cols_rows(sentence_matrix)


def main():
    test_cases = int(sys.stdin.readline())
    for i in range(test_cases):
        sentence = sys.stdin.readline()
        print("Case #{}:".format(i+1))
        palindrome_check = check_palindrome(sentence)
        if palindrome_check == -1:
            print("No magic :(")
        else:
            print(palindrome_check)


main()
