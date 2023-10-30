# Python program to capitalize
# first and last character of
# each word of a String

print()
print("Approach 2: indexing")
# Function to do the same
def word_both_cap(str):

	# lambda function for capitalizing the
	# first and last letter of words in
	# the string
	return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
						s.title().split()))


# Driver's code
s = "welcome to thundersoft"
print("String before:", s)
print("String after:", word_both_cap(str))

print()
print("Approach 2: Using slicing and upper(),split() methods ")

# Python program to capitalize
# first and last character of
# each word of a String

s = "welcome to thundersoft"
print("String before:", s)
a = s.split()
res = []
for i in a:
	x = i[0].upper()+i[1:-1]+i[-1].upper()
	res.append(x)
res = " ".join(res)
print("String after:", res)
