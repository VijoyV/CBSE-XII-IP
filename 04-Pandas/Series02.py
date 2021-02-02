import pandas as pd

print('A simple Python Dictionary')
calories = {"day1": 420, "day2": 380, "day3": 390}
print(calories)

# creating a Pandas series from a python dictionary
# The keys of the dictionary become the labels.

print('Creating Pandas Series from simple Python Dictioanry')
myvar = pd.Series(calories)
print(myvar)

# Create a Series using only data from "day1" and "day2":

print('Creating Pandas Series from Python Dictioanry')
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
