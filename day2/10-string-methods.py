# String Methods

# What are string methods?
# Python has built-in methods that help you modify, check, or analyze text.

# Important rule:
# String methods return a new string. They do not change the original one.

# Example
text = "hello"
print(text.upper())
print(text)

# Output:
# HELLO
# hello

# The original string does not change.

# Programs often modify text when processing user input, cleaning data, or formatting output.

# -------------------------------

# Common string methods (most useful ones)

# upper()
# Converts text to uppercase

text = "hello"
print(text.upper())

# Output: HELLO

# -------------------------------

# lower()
# Converts text to lowercase

text = "HELLO"
print(text.lower())

# Output: hello

# -------------------------------

# strip()
# Removes spaces from the beginning and end.

text = "  hello  "
print(text.strip())

# Output: hello

# Use case: Cleaning user input from forms or APIs.

# -------------------------------

# replace()
# Replaces part of a string with another value.

text = "Hello World"
print(text.replace("World", "Python"))

# Output: Hello Python

# Use case: Editing messages, filenames, or text content.

# -------------------------------

# split()
# Splits text into a list of parts.

text = "apple, banana, cherry"
print(text.split(","))

# Use case: Parsing CSV data, tags, or user input.

# -------------------------------

# find()
# Searches for text and returns its position.

text = "Hello World"
print(text.find("World"))

# Output: 6

# -------------------------------

# count()
# Counts how many times a value appears.

text = "banana"
print(text.count("a"))

# Output: 3

# -------------------------------

# startswith()
# Checks if text starts with something.

text = "hello world"
print(text.startswith("hello"))

# Output: True

# -------------------------------

# endswith()
# Checks if text ends with something.

text = "file.txt"
print(text.endswith(".txt"))

# Output: True

# -------------------------------

# title()
# Capitalizes the first letter of each word.

text = "hello world"
print(text.title())

# Output: Hello World

# -------------------------------

# Simple way to remember

# String methods help you:

# change text       -> upper(), lower(), replace()
# clean text        -> strip()
# split text        -> split()
# search text       -> find(), count()
# check text        -> startswith(), endswith()
