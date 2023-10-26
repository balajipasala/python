test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
replace_char = '$'
retain_char = 'G'

res = [item if item == retain_char else replace_char for item in test_list]
print(res)