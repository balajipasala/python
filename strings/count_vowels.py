
print()
print("Approach 1")

string = "Hello Thundersoft"
vowels = "aeiouAEIOU"

count = sum(string.count(vowel) for vowel in vowels)
print(count)


print()
print("Approach 2")


# Function to count vowel
def vowel_count(str):
	
	# Initializing count variable to 0
	count = 0
	
	# Creating a set of vowels
	vowel = set("aeiouAEIOU")
	

	for alphabet in str:
	
		# If alphabet is present
		# in set vowel
		if alphabet in vowel:
			count = count + 1
	
	print("No. of vowels :", count)
	
# Driver code
str = "Hello Thundersoft "

# Function Call
vowel_count(str)
