# python code to demonstrate summation 
# using reduce() and accumulate() 

# importing itertools for accumulate() 
import itertools 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [1, 3, 4, 10, 4] 

# printing summation using accumulate() 
print("The summation of list using accumulate is :", end="") 
print(list(itertools.accumulate(lis, lambda x, y: x+y))) 

# printing summation using reduce() 
print("The summation of list using reduce is :", end="") 
print(functools.reduce(lambda x, y: x+y, lis)) 
