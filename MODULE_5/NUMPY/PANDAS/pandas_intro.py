import pandas as pd
lst = ['mec','minor','stud','eee','bio']
df = pd.DataFrame(lst)
print(df)

list = {
'Column 0': ['mec', 'minor', 'stud', 'eee', 'bio'],
'Column 1': ['data1', 'data2', 'data3', 'data4', 'data5']
}
dif = pd.DataFrame(list)
print(dif)