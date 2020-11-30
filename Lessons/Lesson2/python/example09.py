# Example 9 - Functions

# We define a function with no arguments
def printHello():
    print('Hello')
    
# We define a function with one argument
def printVariable(n):
    print('This is the variable that you passed:', n)


# We define a function to do an operation
def sumVariables(a,b):
    return a+b

# Use the functions
printHello()

printVariable(100)
printVariable(10.0)
printVariable('a string of characters')

print('The sum of the 5 and -3 is : ', sumVariables(5,-3))
