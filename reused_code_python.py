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


#count in list
import collections
a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
counter=collections.Counter(a)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]

# create a set out of a list
chars = sys.stdin.readline()[:-1]
chars_set = set(chars)
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

#string/char manipulation
x.islower()
x.isupper()
x.lower()
x.upper()