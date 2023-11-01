
n=4 

def patern(n):
	if n==0:
	 	print("value should be more than 0") 
	else:
		patern(n-1)
		print("*"*n)

patern(n)