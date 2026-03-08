# Escape Characters

# What is an escape character
# Somethimes you want to include special characters inside a string, but Python would normally reat them as part of the syntax.

# To solve this, python uses an escape character.

# The escape character is a backslash "\" followed by another character.

# Example: quotes inside a string
# This code causes an error.

# txt = "We are the so-called "Vikings" from the north"

# Because Python thinks the string ends before "Vikings".

# Solution: escape the quotes.

# Use \" to tell Python this quote is part of the text.

# Example:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Output: We are the so-called "Vikings" from the north.

# Escape characters are useful when handling text that contains quotes, like user messages or JSON data.

# -------------------------------------

# Common escape characters

# Single quote
# \'

# Example:
txt = 'It\'s a nice day'

# ------------------------

# Backslash
# \\

txt = "This is a backslash: \\"

# used when working with file paths.

# ------------------------

# New line
# \n

# Example
print("Hello \n World")

""" 
Output :
Hello
World
"""

# Used when formatting multi-line text or logs.

# ------------------------

# Tab
# \t

# Adds a tab space

# Example:

print("Hello\tWorld")

# Output:
# Hello    World

# Used to align text in tables or logs.

# ------------------------

# Other escape characters
# Less commonly used:

# \r        carriage return
# \b        backspace
# \f        form feed
# \ooo      octal value
# xhh       hecadecimal value
