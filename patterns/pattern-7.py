n=5
i=0

while(i<=n):
	print(" "*(n-i) + "* "*i)
	i +=1

for row in range(1, n+ 1):
    print(" " * row +"* " * (n - row))