name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff', 'boom']
animal = ['Cat', 'Dog', 'Fish', 'Goat', 'lion']
age = [1, 2, 2, 6, 7]
z = zip(name, animal, age)
for name,animal,age in z:
    print("%s the %s is %s" % (name, animal, age))