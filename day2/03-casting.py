# Python Casting

# What is casting?
# Casting means converting a value from one data type to another.

# Example
# You might convert a string into a number if you want to do math with it.

# Main casting functions
# Python uses 3 common functions for casting:

# int()     # -> converts to an integer
# float()   # -> converts to a decimal number
# str()     # -> converts to text

# -----------------------

# Conerting to integers (int())

# int() converts values into whole numbers.

# Example

x = int(1)      # 1
y = int(2.0)    # 2
z = int("3")    # 3

# Important:
# If you convert a float to an int, the decimal part is removed.

# Real-world example:
# You might convert a price or measurement into a whole number when decimals are not needed.

# -----------------------

# Converting to floats (float())
# float() converts values into decimal numbers.

# Example
x = float(1)        # 1.0
y = float(2.8)      # 2.8
z = float("3")      # 3.0
w = float("4.2")    # 4.2

# Real-world example:
# You may convert numbers to float when wokring with money, percentages, or measurements.

# -----------------------

# Converting to strings (str())
# str() converts values into text.

# Example
y = str(2)
z = str(3.0)

# Output:
# 2
# 3.0

# Real-world example:
# You often convert numbers to strings when displaying them in messages.

# Example:
age = 25
print("I am " + str(age) + " years old")

# -----------------------

# Simple way to remember
# int() -> whole number
# float() -> decimal number
# str() -> text
