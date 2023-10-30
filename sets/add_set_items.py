# adding set items but you can't change the values.
fruits = {"apple","mango", 'mango', 1, 1}
fruits.add('orange')
print(fruits)

fruits = {"apple","mango", 'mango', 1, 1}
persons_likes_fruits= {'guna', 'prabhas'}
fruits.update(persons_likes_fruits)
print(fruits)