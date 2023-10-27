# Python3 program to find common elements 
# in three lists using sets

print()
print("=======Approach 2: Using Intersection ============")

def IntersecOfSets(arr1, arr2, arr3):
	# Converting the arrays into sets
	s1 = set(arr1)
	s2 = set(arr2)
	s3 = set(arr3)
	

	set1 = s1.intersection(s2)		 #[80, 20, 100]
	result_set = set1.intersection(s3)

	final_list = list(result_set)
	print(final_list)

# Driver Code
if __name__ == '__main__' :
	
	arr1 = [1, 5, 10, 20, 40, 80, 100]
	arr2 = [6, 7, 20, 80, 100]
	arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
	
	# Calling Function
	IntersecOfSets(arr1, arr2, arr3)

print()
print("=======Approach 2: Using Set ============")

def find_common(list1, list2, list3):
	common = set()
	for elem in list1:
		if elem in list2 and elem in list3:
			common.add(elem)
	return common

list1 = [1, 5, 10, 20, 40, 80]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common(list1, list2, list3)
print(common)
