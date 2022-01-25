# my_string = 'Hello'
# print(my_string)

# my_string = "Hello"
# print(my_string)

# my_string = '''Hello'''
# print(my_string)

# # triple quotes string can extend multiple lines
# my_string = """Hello, welcome to
#            the world of Python"""
# print(my_string)

#Note = slicing same as list and tuple

#String concetination

# Python String Operations
# str1 = 'Hello'
# str2 ='World!'

# # using +
# print('str1 + str2 = ', str1 + str2)

# # using *
# print('str1 * 3 =', str1 * 3)

# Some Built function like enumerate

# str = 'cold'

# # enumerate()
# list_enumerate = list(enumerate(str))
# print('List enumerate = ', list_enumerate)
# #character count length
# print('len(str) = ', len(str))

# string escaping

# # using triple quotes
# print('''He said, "What's there?"''')

# # escaping single quotes
# print('He said, "What\'s there?"')

# # escaping double quotes
# print("He said, \"What's there?\"")

# Raw String:-
#without raw string

# print("This is \x61 \n string. ") 

# Raw string
print(r"This is \x61 \n string. ")

# String formatting

# Python string format() method

# default(implicit) order
# default_order = "{}, {} and {}".format('John','Bill','Sean')
# print('\n--- Default Order ---')
# print(default_order)

# # order using positional argument
# positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# print('\n--- Positional Order ---')
# print(positional_order)

# # order using keyword argument
# keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# print('\n--- Keyword Order ---')
# print(keyword_order)


# slpit 
str = "This will split all words into a list"
print(str)
split_str = str.split()

print(split_str)

join_str = ' '.join(split_str)
print(join_str)