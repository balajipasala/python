import pandas as pd
import numpy as np
dic = [{'raj':1,'ram':2},{'suraj':5,'mahesh':4},{'raj':5,'shyam':9}]
out = pd.DataFrame(dic,index=['a','b','c'])
print(out)
print(type(out))

del out['mahesh']

print(out)
