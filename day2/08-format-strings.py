# Format Strings

# The problem: In Python, you cannot directly combine text and numbers with "+"
# Example

age = 30
txt = "My name is John, I am " + age
print(txt)

# This causes an error, beacuse Python cannot join a stirng and a number using "+"

# Solution: f-strings

# The modern way to combine text and values is f-string.

# You add f before the string and use {} as placeholders.

# Example

age = 35
txt = f"My name is John, I am {age}"

print(txt)

# Output: My name is John, I am 35

# This is commonly used to build messages, reports, or UI text.

# Placeholders
# Anything inside {} is called a placeholder.
# It inserts the value into the string

# Example

price = 40
txt = f"The price is {price} dollars"
print(txt)

# Output: The price is 40 dollars

# Used for displaying prices, used data, or statistics.

# -----------------------------------

# Formatting values
# You can format numbers using modifiers.

# Example:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Output: The price is 59.00 dollars
# .2f means show 2 decimal places.
#
# # This is useful when displaying money or percentages

# -----------------------------------

# Using expressions inside placeholders
# You can run Python code inside "{}"

# Example

txt = f"The price is {20 * 59} dollars"
print(txt)

# Output: The price is 1180 dollars

# This is useful when showing calculated results inside messages.
