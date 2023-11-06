import pandas as pd
import numpy as np

s1=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s1)
print(type(s1))

s2=pd.Series({'a':23,'b':34,'c':45})
print(s2)
print(type(s2))