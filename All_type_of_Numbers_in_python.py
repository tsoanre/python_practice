# int a = 5
# float a = 5.0
# complex = x + yj here is the real part and y is the imaginary part.

# example:-

# a = 5
# print(type(a))

# b = 5.0 
# print(type(b))

# print(type(8.0))

# c = 5 + 3j
# print(c + 5) # In complex if we added 5 here then it will add 5 in the real number. 
# print(type(c)) 

# To check that our variable is belongs to class then we use function isinstance()

# print(isinstance(c,complex))  # it returns output in bool.
# print(isinstance(a,int))
# print(isinstance(b,float))

#Numbering in python

# The numbers we deal with every day are of the decimal (base 10) number system. But computer programmers (generally embedded programmers) need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.

# In Python, we can represent these numbers by appropriately placing a prefix before that number. The following table lists these prefixes.

# Number System       	Prefix
# Binary	              '0b' or '0B'
# Octal              	  '0o' or '0O'
# Hexadecimal           '0x' or '0X'

# # examples
# # Output: 107
# print(0b1101011)

# # Output: 253 (251 + 2)
# print(0xFB + 0b10)

# # Output: 13
# print(0o15)



# Note :- We can convert one type of number into another. This is also known as coercion.
# 1. int to float
# 2. Float to int etc.

# but in this example:-

# a = 5.1
# b = 3.2
# c = a+b
# print(int(c))
# print(isinstance(c,int)) # here in output it is not inetger because computer work in binary it does not give approximate result.

# to solve this issues import decimal after converstion it becomes integer
# DECIMAL IN PYTHON
# import decimal

# a = 5.1
# b = 3.2
# c = a+b
# d = int(decimal.Decimal(c))
# print(d)
# print(isinstance(d,int))

# FRACTION IN PYTHON

# Example for integer

# import fractions

# print(fractions.Fraction(1.5))

# print(fractions.Fraction(5))

# print(fractions.Fraction(1,3))


# Example for float

# import fractions
# print(fractions.Fraction(2.6))

# Use of math module
#Example
# import math

# print(math.pi)

# print(math.cos(math.pi))

# print(math.exp(10))

# print(math.log10(1000))

# print(math.sinh(1))

# print(math.factorial(6))

# use random module
