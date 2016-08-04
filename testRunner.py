import mylib, pandas

#print (mylib.isPal(10203))
#print mylib.isPal(102030201)

resultsList = []

for i in range (0, 100):
    resultsList.append(mylib.randomInteger(10,19))

from collections import Counter
counts = Counter(resultsList)
df = pandas.DataFrame.from_dict(counts, orient='index')
df.plot(kind='bar')
print (df)
