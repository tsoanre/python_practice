# global vaiable
# Example 1
# x = "global"
# def func():
#     print(" x inside:",x)

# func()
# print("x outside:",x)

#example 2

# x = "global"

# def foo(x):
#     x = x * 2
#     print(x)
# print("x outside:",x)
# foo(5)

#local variable
#example
# def foo():
#     y = "local"


# foo()
# print(y)  # it will throws error becuase from local variable cannot access from outside.

#example
# def foo():
#     y = "local"
#     print(y)

# foo()

# global and local both
# x = 5

# def foo():
#     x = 10
#     print("local x:", x)


# foo()
# print("global x:", x)

# creating nonlocal variable
# both inner and outer becomes nonlocal variable.
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer() 