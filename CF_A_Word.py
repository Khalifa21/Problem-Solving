import sys
word = sys.stdin.readline()[:-1]
lower_num = 0
upper_num = 0
for i in range(len(word)):
    if word[i].islower():
        lower_num +=1
    else:
        upper_num +=1
if upper_num > lower_num:
    output_word = word.upper()
else:
    output_word = word.lower()

print(output_word)