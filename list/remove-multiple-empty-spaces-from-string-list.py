test = ['hello', ' ', 'hi', '     ', 'book', '  ']

print("original test :" + str(test))

res=[]

for item in test:
	if item.strip():
		res.append(item)

print("After removing empty items: " + str(res))
