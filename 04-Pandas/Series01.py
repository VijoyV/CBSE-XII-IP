import pandas as pd

print('Simple Python List:')

a = [1, 7, 2]
print(a)

print('Create a simple Pandas Series from the list:')

myvar = pd.Series(a)
print(myvar)

print('Return the Second value of the Series:')

print(myvar[1])

print('With the index argument, you can name your own labels.')

myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

print('When you have created labels, you can access an item by referring to the label')
print('Return the value of "y":')

print(myvar["y"])
