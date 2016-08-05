"""
This file is used to test the functions in mylib.py.
"""

from collections import Counter
#import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
#import pandas.io as web

import mylib

#print (mylib.isPal(10203))
#print mylib.isPal(102030201)

#plt.plot([1,2,3],[5,7,4])
#plt.show()

#results_list = [4, 4, 4, 5, 6, 6, 6]
#df = pd.DataFrame.from_dict(counts, orient='index')

results_list = []

for i in range(0, 100):
    results_list.append(mylib.random_integer(10, 19))

#counts = Counter(resultsList)
counts = Counter([4, 4, 4, 5, 6, 6, 6])
df = pd.DataFrame.from_dict(counts, orient='index')
df.plot(kind='bar')
df.show()
