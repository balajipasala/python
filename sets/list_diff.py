
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35, 67]

temp1=[]

for item in li1:
	if item not in li2:
		temp1.append(item)
print(temp1)

temp2=[]
for item1 in li2:
	if item1 not in li1:
		temp2.append(item1)
print(temp2)