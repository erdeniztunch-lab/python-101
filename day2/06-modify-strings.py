# Modify Strings
# Python provides built-in methods to change or process strings.

# ---------------------------------

# Upper case
# upper() converts all characters to capital letters.

# Example:
a = "Hello, World!"
print(a.upper())

# Output: HELLO, WORLD!

# Sometimes systems convert text to uppercase to make comparisons easier (like usernames or product codes).

# ---------------------------------

# Lower case
# lower() converts all characters to small letters.

# Example
a = "Hello, World!"
print(a.lower())

# Output: hello, world!

# Often used when normalizing text, for example when checking search queries or emails.

# ---------------------------------

# Remove whitespace
# Whitespace means spaces before or after text

# strip() removes these spaces.

# Example:

a = " Hello, World! "
print(a.strip())

# Output: Hello, World!

# User input often contains extra spaces, so programs clean it before processing.

# ---------------------------------

# Replace text
# replace() replaces part of a string with another value.

# Example
a = "Hello, World"
print(a.replace("H", "J"))

# Output: Jello, World

# Used when correcting text or replacing keywords in messages or files.

# ---------------------------------

# Split string
# split() divides a string into parts and returns a list.

# Example

a = "Hello, World!"
print(a.split(","))

# Output: ['Hello', 'World!']

# Used to break text into pieces, like splitting CSV data, names, or sentences.
