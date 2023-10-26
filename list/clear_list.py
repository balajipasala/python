print()
print("=======Approach 1 =========")

list1 = [6, 0, 4, 1]
print('list1 before clear:', list1)
 
# Clearing list
list1.clear()
print('list1 after clear:', list1)

print()
print("=======Approach 2 : Clear a List by Reinitializing the List  =========")

list1 = [1, 2, 3]
 
# Printing list2 before deleting
print("List1 before deleting is : "
      + str(list1))
 
# deleting list using reinitialization
list1 = []
 
# Printing list2 after reinitialization
print("List1 after clearing using reinitialization : "
      + str(list1))


print()
print("=======Approach 3 : Clearing a List Using del =========")

list1 = [1, 2, 3]
 
print("List1 before deleting is : " + str(list1))
 
del list1[:]
print("List1 after clearing using del : " + str(list1))

print()
print("=======Approach 3 : pop() method To Clear a List =========")

list1 = [1, 2, 3]
 
print("List1 before deleting is : " + str(list1))
 
while(len(list1) != 0):
    list1.pop()
print("List1 after clearing using del : " + str(list1))

