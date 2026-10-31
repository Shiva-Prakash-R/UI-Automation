# ==========================================
# PYTHON STRING METHODS - COMPLETE PROGRAM
# ==========================================

text = "  Hello Python World  "
print("Original string:", repr(text))

# 1. upper() - Convert to uppercase
print("upper():", text.upper())

# 2. lower() - Convert to lowercase
print("lower():", text.lower())

# 3. capitalize() - Capitalize first character
print("capitalize():", text.capitalize())

# 4. title() - Capitalize each word
print("title():", text.title())

# 5. swapcase() - Reverse letter cases
print("swapcase():", text.swapcase())

# 6. strip() - Remove spaces from both ends
print("strip():", text.strip())

# 7. lstrip() - Remove spaces from the left
print("lstrip():", repr(text.lstrip()))

# 8. rstrip() - Remove spaces from the right
print("rstrip():", repr(text.rstrip()))

# 9. replace() - Replace text
print("replace():", text.replace("Python", "Java"))

# 10. split() - Convert string into a list
print("split():", text.split())

# 11. split(maxsplit) - Limit the number of splits
print("split(maxsplit=1):", text.split(maxsplit=6))

# 12. join() - Join strings using a separator
words = ["Python", "is", "easy"]
print("join():", " ".join(words))

# 13. find() - Find the first position
print("find():", text.find("Python"))

# 14. rfind() - Find the last position
print("rfind():", text.rfind("o"))

# 15. index() - Find position; error if not found
print("index():", text.index("World"))

# 16. count() - Count occurrences
print("count():", text.count("o"))

# 17. startswith() - Check beginning
print("startswith():", text.startswith("  Hello"))

# 18. endswith() - Check ending
print("endswith():", text.endswith("  "))

# 19. isalpha() - Check whether all are letters
print("isalpha():", "Python".isalpha())

# 20. isdigit() - Check whether all are digits
print("isdigit():", "12345".isdigit())

# 21. isalnum() - Check whether all are letters or digits
print("isalnum():", "Python123".isalnum())

# 22. islower() - Check lowercase
print("islower():", "python".islower())

# 23. isupper() - Check uppercase
print("isupper():", "PYTHON".isupper())

# 24. istitle() - Check title case
print("istitle():", "Hello Python".istitle())

# 25. isspace() - Check whitespace only
print("isspace():", "   ".isspace())

# 26. isdecimal() - Check decimal digits
print("isdecimal():", "123".isdecimal())

# 27. isnumeric() - Check numeric characters
print("isnumeric():", "123".isnumeric())

# 28. isidentifier() - Check valid Python identifier
print("isidentifier():", "user_name".isidentifier())

# 29. isprintable() - Check printable characters
print("isprintable():", "Hello".isprintable())

# 30. zfill() - Add zeros to the left
print("zfill():", "42".zfill(5))

# 31. center() - Center the string
print("center():", "Python".center(12, "-"))

# 32. ljust() - Align text to the left
print("ljust():", "Python".ljust(10, "-"))

# 33. rjust() - Align text to the right
print("rjust():", "Python".rjust(10, "-"))

# 34. partition() - Split into three parts
print("partition():", "Python is easy".partition("is"))

# 35. rpartition() - Partition at the last occurrence
print("rpartition():", "a-b-c".rpartition("-"))

# 36. removeprefix() - Remove a prefix if present
print("removeprefix():", "Hello Python".removeprefix("Hello "))

# 37. removesuffix() - Remove a suffix if present
print("removesuffix():", "report.pdf".removesuffix(".pdf"))

# 38. expandtabs() - Replace tabs with spaces
print("expandtabs():", "Hello\\tPython".expandtabs(4))

# 39. format() - Insert values into a string
print("format():", "My name is {} and I am {} years old".format("Shiva", 34))

# 40. format_map() - Format using a dictionary
data = {"name": "Shiva"}
print("format_map():", "Hello {name}".format_map(data))

# 41. encode() - Convert string to bytes
print("encode():", "Hello".encode())

# 42. casefold() - Strong lowercase conversion for comparisons
print("casefold():", "PYTHON".casefold())

# 43. len() - Built-in function: count characters
print("len():", len("Python"))

# 44. str() - Built-in function: convert a value to string
print("str():", str(123))

# 45. ord() - Built-in function: character to Unicode number
print("ord():", ord("A"))

# 46. chr() - Built-in function: Unicode number to character
print("chr():", chr(65))

# 47. min() - Built-in function: smallest character by code point
print("min():", min("Python"))

# 48. max() - Built-in function: largest character by code point
print("max():", max("Python"))

# 49. sorted() - Built-in function: sort characters
print("sorted():", sorted("python"))

# 50. reversed() - Built-in function: reverse character iteration
print("reversed():", "".join(reversed("Python")))
