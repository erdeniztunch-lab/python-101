# Python Numbers
# Python has three main number types

# int
# float
# complex

# When you assign a number to a variable, Python automatically choose the correct type.

# Example:

import random
x = 1    # int
y = 2.5  # float
z = 1j   # complex

# You can check the type with type()
print(type(x))
print(type(y))
print(type(z))

# -----------------------------------

# 1- int -> whole numbers
# An int (integer) is a number without decimals.
# It can be positive or negative

# Example
x = 1
y = 35656222554887711
z = -3255522

# Real-word example:
# Integers are used for counts, like number of users, items in a cart, or page views.

# -----------------------------------

# 2- float -> decimal numbers
# A float is a number that has decimals.

# Example:
x = 1.10
y = 1.0
z = -23.45

# Real-world example:
# Floats are used for measurements, like price, temperature, weight, or percentages.

# Example:
price = 19.99
temperature = 23.5

# Scientific notation
# Floats can also be written using scientific notation with e.

# Example:
x = 35e3
y = 12E4
z = -97.9e100

# Example meaning: 35e3 = 35000

# Real-world use:
# Scientific notation is used for very large or very small numbers, like scientific data.

# -----------------------------------

# 3- complex -> complex numbers
# Complex numbers nontain a real part and an imaginary part.

# Example:

x = 3+5
y = 5j
z = -5j

# Real-word example:
# Complex numbers are used in engineering, physics, and signal processing.

# Beginners rarely use them.

# -----------------------------------

# Converting number types.
# You can convert numbers using:

# int()
# float()
# complex()

# Example:

x = 1
y = 2.9
z = 3

a = float(x)
b = int(y)
c = complex(z)

# Real-world example:
# You often convert types when processing user input or API data.

# Example

age = int("25")

# -----------------------------------

# Important rule
# You cannot convert a compex number to int or float.

# -----------------------------------

# Random numbers
# Python has a module called "random" for generating random numbers.

# Example:


print(random.randint(1, 10))

# This prints a random number between 1,9

# Real-world example:
# Random numbers are used for games, simulations, passwords, or testing data.
