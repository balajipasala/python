# Python Operators
#Arithmetic Operators
'''
1)Arithmetic operators
+ Addition 
- Subtraction 
* Multiplication 
/ Division
% modulus
** Exponentiation 
// Floor Division 
'''
# Addition 
a = 20
b = 25
print(a+b)

# Example 2
x = 20
y = x+20
print(y)

# Subtraction 
y = 165
z = 65
print(y-z)

# Subtraction using function
def subtraction(a, b):
    return a-b
    
x = subtraction(165, 65)
print(x)

#Multiplication
x = 10
y = 20
z = x*y
print(f'the multiplication of {x} and {y} is:- {z}'.format(x, y, z))

# Division
x = 10
y = 2
print(x/y)

#Modulus 
x = 20
y = 10
print(x % y)

#Exponentiation 
z = 2
y = 5
print(2 ** 5)

# //Floor Division
x = 10//2
print(x)
