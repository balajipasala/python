print()
print("Approach 1: loop and flags ")

def checkString(str):

	# initializing flag variable
	flag_l = False
	flag_n = False

	# checking for letter and numbers in
	# given string
	for i in str:

		# if string has letter
		if i.isalpha():
			flag_l = True

		# if string has number
		if i.isdigit():
			flag_n = True

	# returning and of flag
	# for checking required condition
	return flag_l and flag_n


# driver code
print(checkString('thishasboth29'))
print(checkString('geeksforgeeks'))


print()
print("Approach 2: Without using builtin methods")