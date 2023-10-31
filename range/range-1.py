# Python3 code to demonstrate the 
# working of range() without step

# using range()
lis1 = list(range(6))
lis2 = list(range(3, 6))
lis3 = list(range(-6, 2))

# initializing list using range, 1 parameter
# only stop parameter
print("List generated using 1 parameter : " + str(lis1)) 

# initializing list using range, 2 parameters
# only step and stop parameters
print("List generated using 2 parameters : " + str(lis2)) 

# initializing list using range, 2 parameter
# only step and stop parameters
print("List generated using 2 parameters with negatives : " + str(lis3)) 
