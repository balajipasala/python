import re
number=input("enter a mobile number with country code:")
a=re.fullmatch("[+91]{3}\s[6-9]\d{9}",number)
if a!= None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")