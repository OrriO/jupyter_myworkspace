import pandas as pd

df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print(df)
df1=pd.get_dummies(df, prefix=['col1', 'col2'])
print(df1)
