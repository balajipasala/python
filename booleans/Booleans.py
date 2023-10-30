# Booleans 
''' 
In programming you often need to know an expression is "True" or "False".
You can evaluate any expression in python, and get one of two answers True or False
when you compare two values, the expression is evaluated and python returns boolen value
'''
print(10>9)
print(10 == 10)
print(10<9)

# printing a message based on condition True or False
python = 100
linux = 85
if python >= linux:
  print("yes! python is greater than linux")
else:
  print("oops! python is not greater than linux")

# boolean function bool() allows you to evaluate any value and that gives True or False
print(bool("hello world"))
print(bool(23))

'''
Any string is True, except empty "",
any integer is True, except 0,
any list, tuple, dict, & set is True except empty one 
'''
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
