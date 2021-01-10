y = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}

l = list(y.items())  # convet the given dict. into list
# In Python Dictionary, items() method is used to return the list
# with all dictionary keys with values.
l.sort()  # sort the list
print('Ascending order is', l)  # this print the sorted list

l = list(y.items())
print(l)
l.sort(reverse=True)  # sort in reverse order
print('Descending order is', l)

dict = dict(l)  # convert the list in dictionary

print("Dictionary", dict)  # the desired output is this sorted dictionary