# Python3 code to demonstrate working of 
# Convert List to List of dictionaries
# Using dictionary comprehension + loop

print()
print("=======  Approach 1 : Using loop + dictionary comprehension   ========")

# initializing lists
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

print("The original list : " + str(test_list))

# initializing key list 
key_list = ["name", "number"]

# loop to iterate through elements
# using dictionary comprehension
# for dictionary construction
n = len(test_list)
res = []
for idx in range(0, n, 2):
	res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})

# printing result 
print("The constructed dictionary list : " + str(res))
