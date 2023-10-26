print()
print("=======  Approach -1: sort in ascending order and print first element ========")

lst = [6,8,3,1,7]
lst.sort()
print("smallest in list is : " ,lst[0])

print()
print("=======  Approach -1: USING MIN METHOD")
lst = [6,8,3,1,7]

print("smallest in list is : " ,min(lst))

print()
print("=======  Approach -1:  compare list elements ")

lst = [6,8,3,1,7]

min1 = lst[0]
for i in range(len(lst)):
	if lst[i]<min1:
		min1 = lst[i]

print("smallest number in lst is : ", min1) 


