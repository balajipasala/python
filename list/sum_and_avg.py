print()
print("=======  Approach -1 : navie method - iteration========")

lst=[1,2,3,4,5]

count = 0

for i in lst:
	count += i
	avg = count/len(lst)
	

print("total : " + str(count))
print("avg: " + str(avg))

print()
print("=======  Approach -2: Using sum() method ========")
lst=[1,2,3,4,5]

count = 0

for i in lst:
	count = sum(lst)
	avg = count/len(lst)
	

print("total : " + str(count))
print("avg: " + str(avg))