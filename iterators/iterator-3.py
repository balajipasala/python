# Sample built-in iterators


print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)
	

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)
	

print("\nString Iteration") 
s = "Geeks"
for i in s :
	print(i)
	

print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
	print("%s %d" %(i, d[i]))
