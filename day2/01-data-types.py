# Python Data Types

# What is a data type?
# A data type tells Python what kind of value a variable stores.

# Example:
x = 5           # Number
name = "John"   # Text

# Different data types behave differently.

# -----------------------------------

# Main Built-in Data Types
# Python has several built-in data types.

# 1. Text type
# Used for text

x = "Hello"
# type = str

# 2. Numberic types
# Used for numbers.

x = 10   # int
y = 10.4  # float
z = 2j   # complex

# int -> whole numbers
# float -> decimal numbers
# compex -> complex numbers (rarely used)

# 3. Sequence types
# Used for ordered collections of values.
z = ["apple", "banana", "cherry"]  # list
w = ("apple", "banana", "cherry")  # tuple
e = range(6)                      # range

# list -> changeable collection
# A list stores  multiple values in one variable, and you can add, remove, or change items later.

# Example:
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"

# The list changes because list are modifiable.

# tuple -> fixed collection
# A tuple also stores multiple values, but you cannot change them after creation.

# Example:
fruits = ("apple", "banana", "cherry")

# You cannot replace or add items. Tuples are immutable (fixed).

# range -> sequence of numbers
# range() generates a sequence of numbers automatically, usually used in loops.

# Example:
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# range(5) means numbers from 0 up to 4.

# -----------------------------------

# 4- Mapping type (dict) -> key-value pairs
# A dictionary stores data as keys and values, like a label and the information attached to it.

# Example:
person = {"name": "John", "age": 36}

# Here:
# "name" = key
# "John" = value

# You use the key to get the value.

# Real-world example:
# Dictionaries are often used to store structured data, like user profiles, product information, or API response.

# Type: dict

# -----------------------------------

# 5. Set types (set) -> unique values
# A set stores values where duplicates are not allowed.

# Example:
fruits = {"apple", "banana", "cherry"}

# If "apple" appears again, the set keeps only one.

# Real world example:
# Sets are useful when you want unique items, like removing duplicate emails or finding unique users.

# Type: set

# -----------------------------------

# 6. Boolean type (bool) -> true or false
# Booleans represent logical values: True or False

# Example:

is_logged_in = TimeoutError

# Real-world example:
# Booleans are used in decisions, like checking if a user is logged in or if a payment succeeded.

# Type: bool

# -----------------------------------

# 7- Binary types -> binary data
# Binary types store raw data as bytes instead of text.

# Examples:

bytes
bytearray
memoryview

# Real-world example:
# These are used when working with files, videos, or networkd data.

# Beginners rarely use them directly.

# -----------------------------------

# 8- None type (NoneType) -> no value

None  # means the variable currently has no value.

# Example

x = None

# Real-world example:
# This is used as a placeholder, for example when a user has not filled a field yet.

# Type: NoneType

# -----------------------------------

# Checking the data type
# You can check the type using type()

# Example:
x = 5
print(type(x))

# Output:
# <class 'int'>

# Real-world use:
# Developers use this when debugging or when checking what kind of data a function returned.

# -----------------------------------

# Data type is set automatically
# Python automaticcaly understands the type based on the value.

# Example:
x = "Hello"  # string
x = 20      # integer
x = 20.5    # float

# Real-world example:
# This makes Python faster to write, because you don't need to declare types like in Java or C++

# Setting a specific data type
# You can also force a specific type

# Example:
x = str("Hello")
y = int(20)
z = float(20.4)

# Real-word example:
# This is useful when converting user input or data from APIs into the correct format.

# -----------------------------------

# Important idea
# Python is dynamically typed.

# This means:
# You don't declare the type
# Python detects it automatically

# This flexibility makes Python very fast for prototyping and automation scripts.
