import re

def count_characters(input_string):
	uppercase_count = len(re.findall(r'[A-Z]', input_string))
	lowercase_count = len(re.findall(r'[a-z]', input_string))
	special_char_count = len(re.findall(r'[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]', input_string))
	numeric_count = len(re.findall(r'[0-9]', input_string))
	
	return uppercase_count, lowercase_count, special_char_count, numeric_count

test_string = "Hello World! 123"
uppercase, lowercase, special_chars, numeric = count_characters(test_string)

print("Uppercase count:", uppercase)
print("Lowercase count:", lowercase)
print("Special character count:", special_chars)
print("Numeric count:", numeric)
