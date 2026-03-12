# String Formatting

# The problem this solves
# When writing programs, you often need to combine text and values.

# You want to print something like:
# The price is 59 dollars

# But the price might be stored in a variable.

# Example:

price = 59

# So the program needs a way to insert variables into text.

# This is called string formatting.

# The modern solution: f-strings
# Since Python 3.6, the recommended way is f-strings.

# To create an f-string, put f before the string.

price = 59
txt = f"The price is {price} dollars"
print(txt)

# Output: The price is 59 dollars

# What is happening:

f"...{price} ..."

# The {} are placeholders.

# Python replaces the placeholder with the value of the variable.

# Placeholders {}
# A placeholder tells Python:
# "Insert a value here"

name = "John"
print(f"My name is {name}")

# Output: My name is John

# Real-world examples
# Printing usernames
# Showing prices
# Generating messages
# Displaying statistics

# Formatting numbers
# Sometimes you want numbers to appear in a specific format.

# Example: show 2 decimal places.

price = 59
print(f"The price is {price:.2f}")

# Output: The price is 59.00

# What .2f means:
# .2 -> two decimals
# f -> floating point number

# Real-world examples:
# Used when showing:
# - Money
# - Financial numbers
# - Measurements

# Using values directly
# You don't always need a variable.

# Example:
print(f"The price is {95:.2f}")

# Output: The price is 95.00

# Python formats the value directly.

# Doing calculations inside {}
# Inside the placeholder you can run Python expressions.

print(f"The price is {20 * 59}")

# Output: The price is 1180

# Python evaluates the expression before printing it.

# Real-world example:
# Total price
# Taxes
# Discounts

# Using variables in calculations

price = 59
tax = 0.25

print(f"The price is {price + (price * tax)}")

# Python calculates the value and prints the result.

# Using conditions inside f-strings
# You can also use if-else expressions.

# Example:

price = 49
print(f"It is very {'Expensive' if price > 50 else 'Cheap'}")

# Output: It is very Cheap

# Running functions inside {}
# You can run functions inside placeholders.

# Example:

fruit = "apples"
print(f"I love {fruit.upper()}")

# Output: I love APPLES

# Using your own functions

# Example:


def feet_to_meters(x):
    return x * 0.3048


print(f"The plane is flying at {feet_to_meters(30000)} meters")


# Formatting large numbers

# Example:

price = 50000
print(f"The price is {price:,}")

# Output: The price is 50,000

# The comma makes numbers easier to read.
