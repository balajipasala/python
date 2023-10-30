# join sets
num = {1, 10, 11, 20, 21, 30, 31, 40, 1, 10}
names = {"guna", "Sekhar", 21, 10}
add = num.union(names) # union() method return's new set with the values of both sets
print(add)

num = {1, 10, 11, 20, 21, 30, 31, 40, 1, 10}
names = {"guna", "Sekhar", 21, 10}
num.update(names) # update() method inserts set 2 values into set 1
print(num)

# intersection_update() 
