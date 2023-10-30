 # string format combines the string's and integer's
'''
format method takes the passed arguments, formats them,
and place them in the string where the placeholers {} are.
'''

age = 23
name = "ram is {} year old"
print(name.format(age))

# format method takes unlimited number of arguments 

python =  100
Linux  =  80
aws    =  85
final_statement = 'i have got {} marks in python, {} in linux and {} in aws'
print(final_statement.format(python, Linux, aws))

# use can also use index number's in placeholders 
python =  100
Linux  =  80
aws    =  85
final_statement = 'i have got {1} marks in Linux, {2} in AWS and {0} in Python'
print(final_statement.format(python, Linux, aws))

# for decimal points we can use {:.2f}
# Named index
cars = "i like a {carname} and it's model is {model}"
print(cars.format(carname = "Jaguar", model="xjs"))
