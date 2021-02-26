# Simply Defining a list and printing it's length

print ('List - Creation, it`s Size')

thislist = ["apple", "banana", "cherry", "apple", "plum"]
print('The created list, thislist = ',  thislist)

print('length of the list', len(thislist))

print ('List - Getting values of it`s members or elements:')

print('First element of the list -> thislist[0]  = ' , thislist[0])
print('Last element of the list -> thislist[ len(thislist) - 1 ] = ' , thislist[ len(thislist) - 1 ])

print('-ve index is used to access elements at the end of a list:')

print('Last element of te list -> thislist[-1] = ', thislist[-1])
print('Second Last element of te list -> thislist[-2] = ', thislist[-2])

# Defining List by a function - list()
# it will take a any sequence data-types like string, list or tuple as argument

myList = list(['banana', 'apple', 'orange'])
print('myList from a list = ', myList)

myList = list(('banana', 'apple', 'orange'))
print('myList from a tuple = ', myList)

myList = list('vijoy.vallachira')
print('myList from a String = ', myList)
