'''
set() methods:- 

1) difference()
2) difference_update()
3) clear()
4) copy()
5) add
6) isdisjoint()
7) issuperset()
8) issubset()
9) union |
10) intersection() & 
11) symmetric_difference()
12) pop()
13) remove()l
14) update()
15) discard

'''
print("================")
# difference() 
my_set = {1,2,3,4,5}
your_set = {1,4,2,6,9}
print(my_set.difference(your_set))
print(my_set)
print("================")
# difference_update
my_set = {1,2,3,4,5}
your_set = {1,4,2,6,9}
print(my_set.difference_update(your_set))
print(my_set) # imp:- notice the difference between difference and differrence_update by seeing my_set vairbale after printing. 
print("================")
# clear()
my_set = {1,2,3,4,5}
my_set.clear()
print(my_set)
print("================")
# copy()
my_set = {1,2,3,4,5}
copy_m = my_set.copy()
print(copy_m)
print("================")
# add()
my_set = {1,2,3,4,5}
my_set.add(100)
print(my_set)
print("================")
#isdisjoint()
my_set = {1,2,3,4,5}
your_set = {12,8,6,9}
isdis_j = my_set.isdisjoint(your_set)
print(isdis_j)
print("================")
# issuperset()
my_set = {1,2,3,4,5}
your_set = {1,2,3,4,5}
super_set = my_set.issuperset(your_set)
print(super_set)
print("================")
# issubset()
my_set = {1,2,3,4,5}
your_set = {1,2,3,4,5}
sub_set = my_set.issubset(your_set)
print(sub_set)
print("================")
# union()
my_set = {1,2,3,4,5}
your_set = {1,2,3,4,5,6}
union = my_set.union(your_set)
print(union)
print("================")
# intersection()
my_set = {1,2,3,4,5}
your_set = {1,2,3,4,6}
inter_section = my_set.intersection(your_set)
print(inter_section)
print("================")
# symmetric_difference
my_set = {1,2,3,4,5}
your_set = {1,2,3,4}
symmetric_difference = my_set.symmetric_difference(your_set)
print(symmetric_difference)
print("================")
# pop() 
my_set = {1,2,3,4,5}
my_set.pop()
print(my_set)
print("================")
# remove()
my_set = {1,2,3,4,5}
my_set.remove(1)
print(my_set)
print("================")
# update()
my_set = {1,2,3,4,5}
your_set = {1,2,3,4,6}
my_set.update(your_set)
print(my_set)
print("================")
# discard()
my_set = {1,2,3,4,5}
my_set.discard(4)
print(my_set)
print("================")