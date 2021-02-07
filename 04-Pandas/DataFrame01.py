import pandas as pd

print('Pandas Version = ', pd.__version__)

print('Converting a Python Dictionary to a Pandas DataFrame')

# Here 'cars': ["BMW", "Volvo", "Ford"] is a dictionary with key as 'cars' (String) and
# value as a list ["BMW", "Volvo", "Ford"] which is having String values 'BMW', 'Volvo', 'Ford',

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

print('Python Dictionary ', mydataset)
myvar = pd.DataFrame(mydataset)

print('Pandas Dataset after conversion')
print(myvar)
