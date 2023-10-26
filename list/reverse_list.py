print()
print("=======Approach 1 : slicing ")

items = [1,2,3,4,5,6,7,8,9]

def reverse_list(list):
	print("before reversing : " + str(items))
	new_list = list[::-1]
	return new_list

print("After reversing : " + str(reverse_list(items)))

print()
print("=======Approach 3 : using reversed function ")

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))

print()
print("=======Approach 2 : using a two-pointer approach")

def reverse_list(arr):
	left =0
	right = len(arr)-1

	while(left<right):
		#swap
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp

		left +=1
		right -=1

	return arr

arr = [1,3,5,7,9,2,4,6,8]
print("Before reverse: " + str(arr))
print("after reverse" + str(reverse_list(arr)))



