# Data Types

# String:

print("Hello"[4])
# Inside of the square brackets tells us which position in the string we are referring to. 
# Because of working in binary the first position is always 0. 

# Interger:

# Whole numbers without any decimal places. 
print(123 + 345)

# Float:

# Floating-point decimal

# Boolean:

# True or false

# How to check the data type?:

name = "9"

print(type(name))

# type casting
print(float(name))

# Subtraction/Addition/Multiplication/Division

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3   
# exponentional

# Priority
# PEMDAS:
# ()
# **
# * /
# + -
# 

# Multiplication and division are equal in priority but the operation to the left will be solved first.

# Rounding
print(round(8 / 2, 2))
# in the second position the 2 communicates to round to the 2nd place. 

result = 4 / 2
result /= 2
print(result)

# F-strings
# This allows to embed values into a string. Data types get converted into a string. 
print(f"Your score is {result}")

