fruits = {'mango', 'orange', 'banana', 'pineapple', 'cherry'}

# remove() - remove an specific element 
fruits.remove('mango')
print(fruits)

# remove() method will raise an error if item is not present in set
try:
    fruits.remove('guava')
    print(fruits)
except KeyError:
    print('guava is not in this set')


# discard() - remove an element
fruits.discard('banana')

# discard() method will not raise an error if item is not present in set
fruits.discard('pear')
print(fruits, "\n 'pear' is not in set, still this won't raise an error")


# pop() - remove a random element from a set
fruits.pop()
print(fruits)