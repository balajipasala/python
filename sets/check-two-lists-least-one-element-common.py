# Python program to check 
# if two lists have at-least 
# one element common
# using traversal of list


print()
print("=======Approach 1: Traversal of List ============")
def common_data(list1, list2):
	result = False

	# traverse in the 1st list
	for x in list1:

		# traverse in the 2nd list
		for y in list2:

			# if one common
			if x == y:
				result = True
				return result 
				
	return result
	
# driver code
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))


print()
print("=======Approach 2: Using Set and Property ============")

# using set and property

def common_member(a, b):
	a_set = set(a)
	b_set = set(b)
	if (a_set & b_set):
		return True
	else:
		return False
		

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_member(a, b))
