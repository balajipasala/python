# program to check wheather the given string is palindrom or not 


print()
print("===========Approach 1 : navie iternation ===========")
def palindrom(a):

	mid = (len(a)-1)//2
	start =0
	last = len(a)-1
	flag =0

	while(start<=mid):
		if(a[start]==a[last]):
			start +=1
			last -=1
		else:
			flag =1
			break;

	if flag ==0:
		print("the given string is a palindrom")
	else:
		print("the given string is not a palindrom")


#symmetric code

def symmetric(a):

	n=len(a)
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2

	start1 = 0
	start2 = mid
	flag = 0
	while(start1 < mid and start2 < n):
		if(a[start1]==a[start2]):

			start1 +=1
			start2 +=1
		else:
			flag =1
			break;

	if flag == 0:
		print("The given string is a symmetric")
	else:
		print("The given string is not a symmetric")



string="amdamd"
palindrom(string)
symmetric(string)


print()
print("===========Approach 2 : slicing ===========")

string = 'amaama'
half = int(len(string) / 2)


first_str = string[:half]
second_str = string[half:]


# symmetric
if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]: 
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')

print()
print("===========Approach 3 : using reversed function ===========")

# code
string ="malayalam"
print("the string is palindrome" if string==reversed(string) else "the string is not palindrome")



