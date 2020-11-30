# Example 6 - Lists of variables (Numerical lists)

# We define a list of floats as
listOfFloats= [1.0,2.0,3.0]
print('List of floats   : ',listOfFloats)

# We define a list of floats as
listOfIntegers= [1,2,3]
print('List of integers : ',listOfIntegers)

#What about a mixed list of floats and integers?
listOfMixed= [1,2.0,3]
print('List of mixed    : ',listOfMixed)

#What is the indexing on the list?
print('First element    : ',listOfMixed[0])
print('Second element   : ',listOfMixed[1])
print('Third element    : ',listOfMixed[2])
# So a list of three elements is indexed from 0 to 2

#You can convert the mixed list to a list of real numbers simply by calling
listOfMixed[0] = float(listOfMixed[0])
listOfMixed[2] = float(listOfMixed[2])
print('List of mixed    : ',listOfMixed)
