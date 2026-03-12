# Booleans
# What is Boolean
# A Boolean represents one of two values:

True
False

# Booleans are used when a program needs to make decisions.

# Real-world example: Checking if a user is logged in.

is_logged_in = True

# Boolean from comparisons
# When you compare two values, Python returns True or False.

# Example
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Output
# True
# False
# False

# Real-world example: Checking if a user is old enough to register.

# ----------------------------

# Booleans in conditions
# Booleans are often used in if statements.

# Example
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Output: b is not greater than a

# -----------------------------

# The bool() function
# The bool() function converts a value into True or False.

# Example
print(bool("Hello"))
print(bool(15))

# Output:
# True
# True

# Because the values contain something.

# -----------------------------

# Most values are True
# Most values in Python return True if they contain something.

# Example

bool("abc")
bool(123)
bool(["apple", "banana"])

# All return: True

# -----------------------------

# Some values are considered False

# Example
bool(False)
bool(None)
bool(0)
bool("")
bool([])
bool({})

# These return: False

# Reason: they are empty values.

# -----------------------------

# Functions can return Boolean values
# A function can return True or False


def myFunction():
    return True


print(myFunction())

# Output: True


# You can use this inside conditions.

# Example:

def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

# Output: YES!

# -----------------------------

# Built-in functions returning Boolean
# Some Python functions return Boolean values.

# Example:

x = 200
print(isinstance(x, int))

# Output: True

# This checks if x is an integer.
