# Python 3 code to demonstrate the 
# working of range() with step

# initializing list using range
# using step
print("List generated using step : " +
	str(list(range(3, 10, 2)))) 

# initializing list using range
# using negative step
print("List generated using negative step : " +
				str(list(range(10, -5, -3))))

# initializing list using range
# using negative step,
# value constraints fail case
print("List generated using step, value constraints fail : " +
								str(list(range(10, -5, 3))))

# initializing list using range
# using 0 step
# error 
print("List generated using 0 step : " +
			str(list(range(3, 7, 0))))
