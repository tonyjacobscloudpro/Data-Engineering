# Features Highlighted
# Basic String Operations: Concatenation, slicing, and indexing.
# Advanced Features: Encoding, decoding, regex for cleaning, and f-strings for formatting.
# Common Use Cases:
# Palindrome check.
# Counting vowels and consonants.
# Reversing strings or words in sentences.
# Practical Applications:
# Removing special characters.
# Text alignment.
# Multi-line string handling.
# This file demonstrates a wide range of practical string manipulation techniques in Python.


# string_operations.py

# 1. String Basics: Concatenation and Length
print("1. String Basics: Concatenation and Length")
string1 = "Hello"
string2 = "World"
concatenated = string1 + ", " + string2 + "!"
print("Concatenated String:", concatenated)
print("Length of String:", len(concatenated))

# 2. String Indexing and Slicing
print("\n2. String Indexing and Slicing")
text = "Python Programming"
print("First character:", text[0])
print("Last character:", text[-1])
print("Substring (1-6):", text[0:6])
print("Reversed string:", text[::-1])

# 3. String Case Transformations
print("\n3. String Case Transformations")
sentence = "Python is Awesome!"
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Capitalize:", sentence.capitalize())

# 4. Splitting and Joining Strings
print("\n4. Splitting and Joining Strings")
csv_line = "apple,banana,cherry"
words = csv_line.split(",")
print("Split string:", words)
joined = " | ".join(words)
print("Joined string:", joined)

# 5. Finding and Replacing
print("\n5. Finding and Replacing")
paragraph = "Python is fun. Python is easy to learn."
print("Find 'Python':", paragraph.find("Python"))
print("Count 'Python':", paragraph.count("Python"))
print("Replace 'Python' with 'Coding':", paragraph.replace("Python", "Coding"))

# 6. Checking String Properties
print("\n6. Checking String Properties")
alphanumeric = "Python123"
space_string = "   "
print("Is Alphanumeric:", alphanumeric.isalnum())
print("Is Alphabetic:", alphanumeric.isalpha())
print("Is Digit:", "1234".isdigit())
print("Is Lowercase:", alphanumeric.islower())
print("Is Uppercase:", "HELLO".isupper())
print("Is Space:", space_string.isspace())

# 7. Trimming Strings
print("\n7. Trimming Strings")
raw_string = "   Hello, Python!   "
print("Original String:", f"'{raw_string}'")
print("Strip spaces:", f"'{raw_string.strip()}'")
print("Strip left spaces:", f"'{raw_string.lstrip()}'")
print("Strip right spaces:", f"'{raw_string.rstrip()}'")

# 8. Formatting Strings
print("\n8. Formatting Strings")
name = "Alice"
age = 30
formatted = f"My name is {name} and I am {age} years old."
print("Formatted String (f-string):", formatted)
template = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String (format method):", template)

# 9. String Encoding and Decoding
print("\n9. String Encoding and Decoding")
original = "Python 🐍"
encoded = original.encode("utf-8")
print("Encoded (bytes):", encoded)
decoded = encoded.decode("utf-8")
print("Decoded String:", decoded)

# 10. Checking Substrings
print("\n10. Checking Substrings")
message = "The quick brown fox jumps over the lazy dog."
print("Contains 'quick':", "quick" in message)
print("Does not contain 'cat':", "cat" not in message)

# 11. Reversing Words in a Sentence
print("\n11. Reversing Words in a Sentence")
sentence = "Python is fun"
reversed_words = " ".join(sentence.split()[::-1])
print("Reversed Words:", reversed_words)

# 12. Counting Vowels and Consonants
print("\n12. Counting Vowels and Consonants")
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

vowels, consonants = count_vowels_and_consonants("Python Programming")
print("Vowels:", vowels)
print("Consonants:", consonants)

# 13. Palindrome Check
print("\n13. Palindrome Check")
def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print("Is 'radar' a palindrome?", is_palindrome("radar"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))

# 14. Removing Special Characters
print("\n14. Removing Special Characters")
import re
text_with_specials = "Hello, @World! #Python123"
cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text_with_specials)
print("Cleaned Text:", cleaned_text)

# 15. Text Justification
print("\n15. Text Justification")
line = "Python"
print("Center aligned:", line.center(20, "-"))
print("Left aligned:", line.ljust(20, "-"))
print("Right aligned:", line.rjust(20, "-"))

# 16. Multi-line Strings
print("\n16. Multi-line Strings")
multi_line = """This is a
multi-line string.
It can span multiple lines."""
print(multi_line)

# End of examples
print("\nAll string operation examples executed successfully!")
