# Merging Dictionaries
dict_1 = {'key1': 1, 'key2': 2}
dict_2 = {'key3': 3, 'key4': 4}

print(dict(dict_1, ** dict_2))
print(dict(**dict_1, ** dict_2))

