#Examples of function 
# Example 1
# name = input("Enter your name:-")

# def wish(greeting):
#     print(("Hello {}, "+ greeting).format(name))
# wish("Good Morning")

# Example 2
# def my_fun(num):
#     if num>=0:
#         return print(num)
#     else:
#         return print(-num)

# innum = int(input("Enter Your number:- "))
# my_fun(innum)


# #Example 3
# def inside_func():
#     x = 20 
#     print("Inside function x = ",x)
# inside_func()
# x = 30
# print("Outside function x = ",x)


# Built in function

#  example 4
# list()
# print(list)


#user define function

def multiplication(x,y):
    multiplication = x*y
    return multiplication
num1 = 5
num2 = 10
print("Multiplication is = ",multiplication(num1,num2))