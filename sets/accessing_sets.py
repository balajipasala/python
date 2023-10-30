# You can't access a sets by using their index or key 
# but you can loop through sets
fruits = {"apple","mango", 'mango', 1, 1}
for i in fruits:
    print(i)
    
# Check the specific value is present or not using in data type.
fruits = {"apple","mango", 'mango', 1, 1}
print("apple" in fruits)