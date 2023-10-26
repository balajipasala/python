test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
print("The original list : " + str(test_list))
k=1
res=[]
for i in test_list:
	freq = test_list.count(i)
	#print("count of {0} is {1}" .format(i,freq) )
	if freq>k and i not in res:
		res.append(i)

print("required elements are : " + str(res))