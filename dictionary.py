# # empty dictionary
# my_dict = {}

# # dictionary with integer keys
# my_dict = {1: 'apple', 2: 'ball'}

# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}

# # using dict()
# my_dict = dict({1:'apple', 2:'ball'})

# # from sequence having each item as a pair
# my_dict = dict([(1,'apple'), (2,'ball')])

# my_dict = {'name':'Tanuj' ,'Rollno':'0832CS181168'}
# print(my_dict['Rollno']) #direct

# #By get method
# print(my_dict.get('name'))

#changing and adding item in dictionary
# my_dict = {'name':'Shubham' ,'Rollno':'0832CS181155'}

# my_dict['Rollno'] = '0832CS181168'
# my_dict['name'] = 'Tanuj'
# print(my_dict)

# Methods of dictionary


# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# print(squares)
# # pop 
# squares.pop(4)
# print(squares)
# # popitem
# squares.popitem()
# print(squares)

# # clear will clear all dictionary 
# squares.clear()
# print(squares)

# # del will delete all dictionary
# del squares
# print(squares) # it will delete complete dictionary so there is no any dictionary or empty dictionary thats why giving error.

# fromkeys use in dictioanary

# marks = {}.fromkeys(['English','Hindi','Maths','physics','chemistry'],90)
# print(marks)
# # to print key and values both
# for item in marks.items():
#     print(item)
# # To print only keys
# print(list(marks.keys()))

# Dictionary comprehension

# squares =  {x : x*x for x in range(10)}
# print(squares)

# Comprehension with if condition

odd_squares = {x : x*x for x in range(20) if x%2==1}
print(odd_squares)  