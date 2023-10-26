
print("=======  Approach -1 ========")
print("swap using temporary variable")
newList = [10, 20, 30, 40]

def swapList(newList):
	size = len(newList)

	#swapping
	temp = newList[0]
	newList[0] = newList[size-1]
	newList[size-1]= temp

	return newList

print(swapList(newList))
print()
print("=======  Approach -2 ========")
print("The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].")


newList2 = ['a', 'b', 'c', 'd']
def swapList(newList):
	newList2[0], newList2[-1] = newList2[-1], newList2[0]
	
	return newList2

print(swapList(newList2))
print()
print("Approach 3: Using * operand. ")

# Swap function
def swapList(list):
     
    start, *middle, end = list
    list = [end, *middle, start]
     
    return list
     
# Driver code
newList3 = [12, 35, 9, 56, 24]
 
print(swapList(newList3))

print()
print("Approach 4: Swap the first and last elements is to use the inbuilt function list.pop().")

def swapList(list):
     
    first = list.pop(0)   
    last = list.pop(-1)
     
    list.insert(0, last)  
    list.append(first)   
     
    return list
     
# Driver code
newList = [1, 3, 9, 5, 4]
 
print(swapList(newList))