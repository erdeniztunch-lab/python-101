# Python Comments

# What are comments?

# Comments are notes in the code that Python ignores. They are used to explain code or make it easier to read.

# Yes, this is a comment too!

# ------------

# Creating a comment

# A comment starts with "#"

# Example

# This is a comment
print("Hello, World!")

# Python ignores the comment and only runs the print() line.

# ------------

# Comment at the end of a line
# You can also place a comment after code

# Example
print("Hello, World!")  # This is a comment

# Python runs the code and ignores everything after "#"

# ----------

# Using comments to disable code

# You can use "#" to stop a line from running while testing.

# Example

# print("Hello, World!")
print("Hello, dude!")

# The first line is ignored because it is commented.

# Multiline comments

# Python does not have a special syntax for multiline comments.
# The common way is to add "#" to each line.

# This is a comment
# written in
# more than one line

# You may also see triple quotes, but they are actually multiline strings, not real comments.

# Example

'''
This is a string
written in
more than one line
'''
print("Hello, World!")

# Python reads the string but ignores it if it is not assigned to a variable.

# Output:
# Hello, World!
