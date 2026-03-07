# Python Strings

# What is a string
# A string is text in Python

# Strings must be written inside quotes

# Example
print("Hello")
print('Hello')

# Both are the same

# Real-world example
# Strings store names, messages, emails, product titles, etc.

# ---------------------------------

# Quotes inside strings
# You can use quotes inside a string if they are different from the outer quotes.

# Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# ---------------------------------

# Assigning a string to a variable
# You can store a stirng in a variable

# Example

a = "Hello"
print(a)

# Real-world example:
# Variables often store user names or messages

name = "Alice"

# ---------------------------------

# Multiline strings
# you can write a string across multiple lines using triple quotes.

# Example
a = '''Hello
This is
Python'''
print(a)

# or

b = """Hello
This is 
Python"""
print(b)

# Real-world example:
# Multiline strings are useful for long text, descriptions, or documentation.

# Strings are like arrays
# A string is a sequence of characters.

# Example

p = "Hello"
print(p[1])

# Output: e

# Because Python counts from 0
# H e l l o
# 0 1 2 3 4

# Real-world example:
# Accessing characters is useful when processing text data.

# ---------------------------------

# Looping through a string
# You can go through each character using a loop

# Example
for x in "banana":
    print(x)

# Output:
# b
# a
# n
# a
# n
# a

# Real-world example:
# This is used in text processing, validation, or parsing input.

# ---------------------------------

# String length
# Use len() to get the length of a string.

# Example
a = "Hello"
print(len(a))

# Output: 5

# You might check if a password has enough characters.

# ---------------------------------

# Check if text exists.
# Use in to check if text exist inside a string.

txt = "The best things in life are free!"
print("free" in txt)

# Output: True

# Checking if a keyword appears in a message or email.

# ---------------------------------

# Check if text does NOT exist
# Use -> not in

# Example
txt2 = "The best things in life are free!"
print = ("expensive" not in txt2)

# Output: True

# Cehcking if forbidden words are not in a message.
