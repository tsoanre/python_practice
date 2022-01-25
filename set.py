# set cannot have duplicate
# set = {1,2,3,'tanuj'}
# empty set 
# s = set()
# print(type(s))

# Methods of set :-
set = {1, 3}
print(set)
# add item
set.add(2)
print(set)

#update items
set.update([4,5,6])
print(set)

#update list and set 

set.update([7,8,9],{10,11,12})
print(set)


# discard an element
# Output: {1, 3, 5, 6}
set.discard(4)
print(set)

# remove an element
# Output: {1, 3, 5}
set.remove(6)
print(set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
set.discard(2)
print(set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

#it shows error because 20 is not present but if we use discard then there is no error it shows none.
# set.remove(20)
 
# dlt 1 from set
# set.pop(1)
print(set)

# dlt last element
set.pop()
print(set)

# to clear
set.clear()
print(set)


#set intersection
# which same in both.
# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

#set union
# Merging both then output get
# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

#Frozen set 
A = frozenset([1,2,3,4,5])
B = frozenset([6,7,8,9,10])

print(A.isdisjoint(B))