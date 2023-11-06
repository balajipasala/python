# Data frame is a 2 dimentional data structure ,like a 2 dimentional array or a table with rows and columns.

import pandas as pd
import numpy as np

s1=pd.DataFrame([[1,2,3,4],[5,3,7,9],[9,8,0,2]],columns=['a','b','c','d'],index=['e','f','g'])
print(s1)
print(type(s1))