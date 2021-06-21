import pandas as pd
data = pd.DataFrame({
    'name':['Amy', 'Bob', 'Charles'],
    'salary':[30000, 50000, 40000]}
    ,index = ['a', 'b', 'c']
    )
print(data)
print('====')

print('Number of data:', data.size)
print('(Row, columns):', data.shape)
print(data.index)
print('====')

print('The second row:', data.iloc[1], sep = '\n')
print('====')

print('The row c:', data.loc['c'], sep = '\n')
print('====') 

print('The name column:', data['name'], sep = '\n')
print('====')

data['revenue'] = [500000, 300000, 400000]
data['rank'] = pd.Series([1, 2, 3], index = ['a', 'b', 'c'])
data['cp'] = data['revenue'] / data['salary']
print(data)

