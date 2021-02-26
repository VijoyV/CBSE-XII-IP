# List - Accessig Items in different ways using Range

print('List - Accessig Items in different ways using Range:')

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print('thislist = ', thislist)

print('element with index 2 (included) to element with index 5-1=4, thislist[2:5] = ', thislist[2:5])
print('it actually prints elements from index 2 to index (5-1=4) - i.e. elements with indexes 2,3,4')

print('beginning of the list, 0th index / or first element till 4th element (excluded) -> thislist[:4]', thislist[:4] )

print('2nd index (actually 3rd element) till end of the list -> thislist[2:]', thislist[2:] )

print('Range of -ve elements -4 to -1 -> thislist[-4:-1] = ', thislist[-4:-1])
