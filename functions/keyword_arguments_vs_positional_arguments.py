''' 
Keyword arguments vs Positional arguments

Keyword arguments are bad practise. 
'''

def greetins(name, age):
    print(f'my name is:{name} and age {age}')
    
# positional arguments  
greetins('Raj', 22) # These are called positional arguments

# keyword arguments
greetins(age = 22, name = 'Raj')

# Default parameters:-

def greetings(name = 'Raj', age = 23): # default arguments 
    print(f'my name is:{name} and age {age}')
    
greetings()
greetings("hello",56) #overiding the default args
     
