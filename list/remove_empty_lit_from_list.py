# Python3 code to Demonstrate Remove empty List
# from List using list comprehension

print()
print("=======  Approach 1 : Using List Comprehension   ========")

test_list = [5, 6, [], 3, [], [], 9]

print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print("List after empty list removal : " + str(res))

print()
print("=======  Approach 2 : Using filter() method   ========")



test_list = [5, 6, [], 3, [], [], 9]


print("The original list is : " + str(test_list))

res = list(filter(None, test_list))

print("List after empty list removal : " + str(res))

print()
print("=======  Approach 3 : Using function defination   ========")


def empty_list_remove(input_list):
	new_list = []
	for ele in input_list:
		if ele:
			new_list.append(ele)
	return new_list

input_list = [5, 6, [], 3, [], [], 9]

print(f"The original list is : {input_list}")
print(f"List after empty list removal : {empty_list_remove(input_list)}")

print()
print("=======  Approach 4 : Using remove method   ========")

test_list = [5, 6, [], 3, [], [], 9]

print("The original list is : " + str(test_list))

while [] in test_list:
	test_list.remove([])

print("List after empty list removal : " + str(test_list))
