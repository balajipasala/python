print()
print("=======Approach 1 : slicing ")
def cloning_list(lst):
	lst_copy = lst[:]
	return lst_copy

lst = [1,2,3,4,5]
lst2= cloning_list(lst)

print("original : " + str(lst))
print("cloned one : " + str(lst2))

print()
print("=======Approach 2 : Using list comprehension ")

def cloning_list(lst):
	lst_copy = [i for i in lst]
	return lst_copy

lst = [2,4,6,8]
lst2= cloning_list(lst)

print("original : " + str(lst))
print("cloned one : " + str(lst2))


