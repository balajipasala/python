# Basic if elif else statements 
# if statement basic code
a = 10
b = 20
if a<b:
    print(f'{a} less than {b}')

# elif statement example
a = 10
b = 20
if a>b:
    print(f'{a} greater than {b}')
elif a<b:
    print(f"{a} less than {b}")
    
    
# else statement 
a = 10
b = 20
if a>10:
    print("yes")
else:
    print("no")
# short hand if statement
a = 10
b = 20
if a<20: print("yes 10 less than 20")
    
#short hand if else statement 
# short hand if statement
a = 10
b = 20
print("yes") if a<b else print("no")


# and logical operator( returns True if both statements are True)
a = 10
b = 20
c = 30
if a<b and c>b:
    print("both statements are True")
    
# or logical operator return True if any one statement is True.
a = 10
b = 20
c = 30
if a<b and a>b:
    print("only one statement is True")
