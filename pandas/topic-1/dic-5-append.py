import pandas as pd
import numpy as np
dic = [{'raj':1,'ram':2},{'suraj':5,'mahesh':4},{'raj':5,'shyam':9}]
out = pd.DataFrame(dic,index=['a','b','c'])
print("Before index change\n")
print(out)


d={'raj':1,'suraj':33,'mahesh':22,'ram':56,'shyam':89}
out1 = pd.DataFrame(d,index=['d'])
#d1 = out.append(d)

print(out.index)
