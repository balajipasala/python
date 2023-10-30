# set methods
'''
add
update
del keyword
pop
clear
discard
remove
copy
union
intersection
intersection_update
symentric_difference_update()
symentric_difference()
difference

'''
# add() method is used to insert a value into set.
fruits = {"orange", "watermelon", "mango"}
fruits.add('mixed-fruit')
print(fruits)

# update() method is used to append the set2 values into set1.
fruits = {"orange", "watermelon", "mango"}
vegetables = {'carrot', 'tamato', 'onion', 'drumstick'}
fruits.update(vegetables)
print(fruits)

#del keyword is used to delete the set
fruits = {"orange", "watermelon", "mango"}
del fruits
