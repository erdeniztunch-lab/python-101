# Python "None"

# In Python, None means "no value" or "nothing here yet."

# Think of it like an empty placeholder.

# Example idea:
# - A variable exists
# - But it does not contain any real value yet

# Example:
x = None
print(x)

# Output: None

# So x exists, but it doesn't store any real data.

# The type of "None"
# Every value in Python has a type.

# The type of None is:
# NoneType

# Example:
x = None
print(type(x))

# Output: <class 'NoneType'>

# Important idea:
# There is only one None value in Python.

# Why "None" exists
# Sometimes a program needs a variable before the real value is known.

# Example situation:
# You create a variable for a search result, but you haven't searched yet.

result = None

# Later the program might update it:

result = "Found user"

# Real-world examples:
# - Waiting for API response
# - Waiting for database result
# - Optional form field that the user has not filled yet

# Checking if something is "None"
# Python recommends checking None using:
# is
# is not

# Example:

result = None

if result is None:
    print("No result yet")
else:
    print("Result is ready")

# Explanation:
# If result has no value -> message appears
# If result contains data -> different message appears

# Why "is" instead of "=="?
# Because None is a special object, so Python checks identity.

# Checking the opposite
# Example:
result = None

if result is not None:
    print("Result is ready")
else:
    print("No result yet")

# This checks if the variable has a real value.

# None in Boolean logic

# Python treats None as False in conditions.

# Example:

print(bool(None))

# Output: False

# Example use:
result = None
if not result:
    print("No data")
# This works because None behaves like False.

# Functions returning None

# If a function does not return anything, Python automatically returns None.

# Example:


def myFunc():
    x = 5


result = myFunc()
print(result)

# Output: None
# Why?
# Because the function did not use "return"


# Simple way to remember
# None = no value
# NoneType = its data type

# It is used when:
# a value doesn't exist yet
# a variable is intentionally empty
