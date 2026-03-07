# Python Variables

# What is a variable?
# A variable is a container that stores data

# Creating variables
# Python does not need a special command to create a variable. A variable is created when you first assign a value.

# Example

x = 5
y = "John"
print(x)
print(y)

# x stores a number
# y stores text

# Variables can change type
# A variable can hold any type of value, and its type can change later.

# Example

i = 4        # int
i = "Hello"  # now str
print(i)

# Python prints "Hello" because the new value overwrites the old one.

# Casting
# You can force a variable to a specific type using casting
e = str(3)      # '3'
w = int(3)      # 3
q = float(3)    # 3.0

# Check variable type
# Use type() to see what type a variable is.

u = 5
s = "John"
print(type(u))  # <class 'int'>
print(type(s))  # <class 'str'>

# Strings: single or double quotes
n = "John"
b = 'John'  # Same thing

# Case-sensitive
# Variable names distinguish uppercase and lowercase

a = 4
A = "Sally"
# a and A are different variables
