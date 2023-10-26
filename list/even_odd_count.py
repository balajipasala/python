# Python program to count Even
# and Odd numbers in a List

print()
print("=======  Approach 1 : count method ========")
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

print()
print("=======  Approach 2 : Using while loop  ========")


list1 = [10, 21, 4, 45, 66, 93, 11]

even_count, odd_count = 0, 0
num = 0

while(num < len(list1)):

	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	
	# increment num 
	num += 1
	
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


print()
print("=======  Approach 3 : Using List Comprehension   ========")

list1 = [10, 21, 4, 45, 66, 93, 11]

only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)

print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)
