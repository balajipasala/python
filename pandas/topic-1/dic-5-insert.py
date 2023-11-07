import pandas as pd
import numpy as np
dic = [{'raj':1,'ram':2},{'suraj':5,'mahesh':4},{'raj':5,'shyam':9}]
out = pd.DataFrame(dic,index=['a','b','c'])
print(out)
print(type(out))

#this adds new data to the new column inserted
d1 = out.insert(4,'dim', [6,4,5])
#this give the same data stored for shyam column
#d1 = out.insert(4,'dim', out['shyam'])


print(out)
