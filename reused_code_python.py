# switch
x,y = y,x

# Get a unicode of a character 
ord(‘a’)

# Get a character of a unicode 
chr(97)

# read a line except /n 
sys.stdin.readline()[:-1]

# Get a permutation of a string 
from itertools import permutations
permutations(input_word)

# Sort and apply a function on the input before sorting
sorted(char_count.keys(), key=str.lower)
sorted(results.items(),key= lambda kv:(kv[1][0], - kv[1][1],-kv[0]), reverse=True)

# Substitute string or multiple strings with another 
re.sub("\n|\t|\r|\r\n", "", input_word)
re.sub('[^A-Za-z]', ' ', sentence)

## reverse a list 
to_stack [::-1]
row_list.reverse()

# end printing with specific format, default is /n
print("{}".format(a), end='')

# copy list
ans[:]

# split string
numbers.split()

# Check if element (key) exists in dict
contest_data.get(c)

# Lists manipulation
list[start:end:step] # if step is negative it goes in reverse order

#bitmaping
(1<<i) & input_number
a = a | (1 << one_indcies[i])

# remove element from list
princess.remove(mn)


# pass by value vs pass by ref
https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
