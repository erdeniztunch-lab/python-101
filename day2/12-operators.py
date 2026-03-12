# Operators

# What are operators?
# Operators are symbols used to perform operations on values or variables.

print(10 + 5)

# Output: 15

# Here "+" is an operator.

# Operators are used in programs to calculate prices, compare values, and make decisions.

# --------------------------------

# 1- Arithmetic Operators
# Used for math operations

# Example

x = 10
y = 4

print(x + y)   # addition
print(x - y)   # subtraction
print(x * y)   # multiplication
print(x / y)   # division
print(x % y)   # remainder
print(x ** y)  # power
print(x // y)  # floor division

# Examples in real life:
# Price calculations
# Statistics
# Finance calculations

# --------------------------------

# 2- Assignment Operators

# Used to store or update values in variables.

# Example

x = 5
x += 3
print(x)

# This means:
x = x + 3

# --------------------------------

# 3- Comparison Operators

# Used to compare values.
# They return True or False.

# Example

x = 6
y = 3

print(x == y)
print(x > y)
print(x < y)

# Output:
# False
# True
# False

# --------------------------------

# 4- Logical Operators

# Used to combine conditions.

# Operators:
# and
# or
# not

# Example:

x = 5
print(x > 0 and x < 10)

# Output: True

# Real-world example: checking if a password is valid AND the user exists.

# or -> at least one condition must be True

# Example:

x = 5
print(x < 3 or x < 10)

# Output: True

# not -> reverses the result
# if something is True, "not" makes it False
# if something is False, "not" makes it True

# Example

x = 5
print(not (x > 3))

# Explanation:
# x > 3 -> True
# not True -> False

"""remember from JS:
and  -> &&
or   -> ||
not  -> !
"""

# --------------------------------

# 5- Identity Operators

# Check if two variables refer to the same object in memory.

# Example

x = [1, 2, 3]
y = x

print(x is y)

# Output: True

# Rarely used by beginners, but helpful when checking if two variables point to the same data.

# --------------------------------

# Difference between == and is

# == -> compares values
# is -> compares memory objects

# Example

x = [1, 2]
y = [1, 2]

print(x == y)
print(x is y)

# Output:
# True
# False

# Why?

# x == y -> True, because both lists contain the same values [1, 2]

# x is y -> False, because Python created two separate list objects in memory.

# "==" compares values. It checks if the content is the same.

# "is" compares objects. It checks if both variables point to the same object in memory.

# --------------------------------

# 6- Membership Operators

# Check if a value exists inside a sequence.

# Operators:
# in
# not in

# Example

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

# Output:
# True
# True

# Real-world example: checking if a user exists in a database list.

# --------------------------------
