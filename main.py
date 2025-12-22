fruits = ("apple", "banana", "cherry", "date", "elderberry")
# Accessing elements by index
print(fruits[-1:-3]) 
print(fruits[-3:-1])#output: ('cherry', 'date')
print(fruits[1:4])  #output: ('banana', 'cherry',
print(fruits[::2])  #output: ('apple', 'cherry', 'elderberry') 'date')
print(fruits[::-1]) #output: ('elderberry', 'date', 'cherry', 'banana', 'apple')
print(fruits[::-2])  #output: ('apple', 'cherry', 'elderberry')


sweets = ("apple", "banana", "cherry", "elderberry")
print(sweets[2:-1]) #output: ('cherry',)
print(sweets[2::-1])#output: ('cherry', 'banana', 'apple')
print(sweets[-1:-4]) #output: () 