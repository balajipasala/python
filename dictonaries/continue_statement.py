# skiping 'name' key and printing remaining all the keys.
this_dict = {"name":"raj", 'age':23, 'door_no': 20.3, 'boo':True}
for i in this_dict:
    if i == 'name':
        continue # with the continue statement we can stop the current iteration, and continue with the next
    print(i)
    
    
