'''
What is while loop?
ANS:- with the while loop we can execuate a set of statements as long as condition is True
'''
# Example 
i = 1
while i<5:
  print(i)
  i = i+1 # remember to increase while loop otherwise loop will continue for ever. 
  
# break statement; with the break statement we can stop the loop even if the condition is True

i = 1
while i<8:
  print(i)
  if i == 6:
    break
  i = i+1
  
# continue statement; with the continue statement we can stop the current iteration, and continue with the next.
j = 5
while j < 10:
    j = j+1
    if j == 7:
        continue
    print(j)
