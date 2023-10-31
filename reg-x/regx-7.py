import re 


# Beginning of String 
match = re.search(r'^Geek', 'Campus Geek of the month') 
print('Beg. of String:', match) 

match = re.search(r'^Geek', 'Geek of the month') 
print('Beg. of String:', match) 

# End of String 
match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks') 
print('End of String:', match) 
