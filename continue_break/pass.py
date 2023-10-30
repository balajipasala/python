# Python program to demonstrate 
# pass statement 

s = "geeks"

# Empty loop 
for i in s: 
	# No error will be raised 
	pass

# Empty function 
def fun(): 
	pass

# No error will be raised 
fun() 

# Pass statement 
for i in s: 
	if i == 'k': 
		print('Pass executed') 
		pass
	print(i) 
