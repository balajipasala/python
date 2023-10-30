# Removing set items 
# Note: remove method takes exactly only one argument.
fruits  = {'apple', 'orange', 'watermelon', 'guvva'}
fruits.remove('orange') # remove method removes the specified value from the set
print(fruits)
# remove method throws an error if the specifed value doesn't exits.

# Discard method won't throw an error if the specifed value doesn't exits. 
fruits  = {'apple', 'orange', 'watermelon', 'guvva'}
fruits.discard('apple')
print(fruits)

'''
pop() method removes last value, but we don't know which value will be removed 
beacuse sets are unordered.
'''
fruits  = {'apple', 'orange', 'watermelon', 'guvva'}
fruits.pop()
print(fruits)

# del keyword deletes entire set
fruits  = {'apple', 'orange', 'watermelon', 'guvva'}
del fruits
print(fruits) # NameError will raise because set is deleted

#clear() method empty's the set
fruits  = {'apple', 'orange', 'watermelon', 'guvva'}
fruits.clear()
print(fruits)
