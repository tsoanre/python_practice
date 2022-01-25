#Anonymous is also known as lambda function.
# syntax:- lambda arguments:expression
# lambda function can have any number of argument but only one expression.
# example 1

# multiplication = lambda x,y: x*y
# print(multiplication(5,5)) 

# example multication with 2 in the list.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)
