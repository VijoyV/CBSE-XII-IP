# List can contain any basic data types and mixture of it.

print('A List may contain any basic data types and mixture of it:')

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print ('lists of same data type:')

print('list1 = ', list1, 'list element type = ', type(list1[0]))
print('list2 = ', list2, 'list element type = ', type(list2[0]))
print('list3 = ', list3, 'list element type = ', type(list3[0]))

print ('A list of mixed data types:')
list4 = ["abc", 34, True, 40, "male"]
print('list4 = ', list4, 'list type = ', type(list4))

print('List element data-types: ')

for element in list4:
    print('element of list4 = ', element, ' and its data-type is ', type(element))
