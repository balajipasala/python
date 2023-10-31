import re 


match = re.search(r'software', 'Thundersoft is s software developement company') 
print(match) 
print(match.group()) 

print('Start Index:', match.start()) 
print('End Index:', match.end()) 
