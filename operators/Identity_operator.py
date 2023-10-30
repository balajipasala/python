'''
Identity operator

Return's True, if both variables are the same objects

'''

x = ['hello', 'world']
y = [1,2,3,4]
z = x
if z is x:
    print('Return\'s True, if both variables are the same objects')
    
else:
    print('It\'s not a Identity operator')
