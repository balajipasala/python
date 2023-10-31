# A simple generator for Fibonacci Numbers 
def fib(limit): 
	
	 
	a, b = 0, 1

	while a < limit: 
		yield a 
		a, b = b, a + b 


x = fib(5) 


print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 


print("\nUsing for in loop") 
for i in fib(5): 
	print(i)
