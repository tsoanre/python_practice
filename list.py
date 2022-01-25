# l = [1,2,3] list 
# l = [] empty list
# l = [1,3.2,'TANUJ']
# l = [1,[1,3,2],['shubham','vidhan','Tanuj']]

# example
# my_list = ['p', 'r', 'o', 'b', 'e']

# # first item
# print(my_list[0])  # p

# # third item
# print(my_list[2])  # o

# # fifth item
# print(my_list[4])  # e

# # Nested List
# n_list = ["Happy", [2, 0, 1, 5]]

# # Nested indexing
# print(n_list[0][1])
# print(n_list[0][3])
# print(n_list[1][2])

# print(n_list[1][3])

# Error! Only integer can be used for indexing
# print(my_list[4.0])

# Negative indexing
# Negative indexing in lists
# my_list = ['p','r','o','b','e']

# # last item
# print(my_list[-1])

# # fifth last item
# print(my_list[-5])

#list slicing

# List slicing in Python

# my_list = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
# print(my_list[2:5])
# print(my_list[3:9])

# # elements from index 5 to end
# print(my_list[5:])
# print(my_list[0:])
# # elements beginning to end
# print(my_list[:])

# Add item or changes in list

# l = [1,2,3,4,5,6]

# l[2] = 4
# l[3:6] = [5,70,500]

# # append and extend method
# l.append(6)
# l.extend([1,2,3,78,956])

# print(l)

#concatenating list

# l = [1,2,3,4,5,6,7]
# print(l + [8,9,10])
# print(l + ['re']*3)

# Methods of list

# my_list = ['p','r','o','b','l','e','m']
# my_list.remove('p')

# # Output: ['r', 'o', 'b', 'l', 'e', 'm']
# print(my_list)

# # Output: 'o'
# print(my_list.pop(1))

# # Output: ['r', 'b', 'l', 'e', 'm']
# print(my_list)

# # Output: 'm'
# print(my_list.pop())

# # Output: ['r', 'b', 'l', 'e']
# print(my_list)

# my_list.clear()

# # Output: []
# print(my_list)

# list comprehension

# power2 = [2 ** x for x in range(10)]
# print(power2)

#second method 
# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)

# list comrehension for odd number
odd = []
for i in range(50):
    if(i%2==1):
        odd.append(i)
print(odd)
