import re
n=input("enter mobile number:")
a=re.fullmatch("[7-9]\d{9}",n)
if a!=None:
    print("vaild number")

else:
    print("invalid number")