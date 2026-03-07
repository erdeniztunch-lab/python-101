# Slicing Strings

# What is slicing
# Slicin means taking a part of a string.

# You do this using:
# [start:end]

# Example

b = "Hello World!"
print(b[2:5])

# Output: llo

# Explanation:
# H e l l o ,   W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11 12

# Python takes characters from index 2 up to 5 (5 not included).

# You might slice strings when extracting usernames, file names, or parts of text.

# ---------------------------------

# Slice from the start
# If you skip the start index, Python starts from the beginning.

# Example

b = "Hello, World!"
print(b[:5])
# Output: Hello

# Getting the first few characters of a product code or ID

# ---------------------------------

# Slice to the end
# If you skip the end index, Python goes to the end of the string.

# Example
z = "Hello, World!"
print(z[2:])

# Output: llo, World!

# Real-world example:
# Extracting the domain from an email.

# ---------------------------------

# Negative indexing
# Negative numbers start counting from the end of the string.

# Example:
a = "Hello, World!"
print(a[-5:-2])

# Output: orl

# Explanation:

# W o r l d !
# -6 -5 -4 -3 -2 -1
