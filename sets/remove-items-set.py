# Python program to remove elements from set
# Using the pop() method

print()
print("=======Approach 1: Using the pop() method ============")
def Remove(initial_set):
	while initial_set:
		initial_set.pop()
		print(initial_set)

# Driver Code
initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)

print()
print("=======Approach 2: Using discard() method: ============")
# initialize the set
my_set = set([12, 10, 13, 15, 8, 9])

# remove elements one by one using discard() method
while my_set:
	my_set.discard(max(my_set))
	print(my_set)


print()
print("=======Approach 2: Using remove() method: ============")
# initialize the set
my_set = set([12, 10, 13, 15, 8, 9])

# remove elements one by one using remove() method
for i in range(len(my_set)):
	my_set.remove(next(iter(my_set)))
	print(my_set)
	
	
