
# Python3 code to demonstrate working of 
# Add Space between Potential Words
# Using loop + join()
 
# initializing list
test_list = ["gfgBest", "forGeeks", "andComputerScience"]
print("The original list : " + str(test_list))
 
res = []
for item in test_list:
	temp = [[]]
	for char in item:
		if char.isupper():
			print("upper char:", item)
			temp.append([])
		temp[-1].append(char)

	res.append(' '.join(''.join(item) for item in temp))

print(res)