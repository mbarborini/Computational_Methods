# Example 4 - Comparison Operators

# We define an integer variable
x = 2
print('x =', x)

# Let's print out the comparison values.
print('So we have that')
print('  x == 2 :', (x == 2)) # ( == Equal )          prints out True
print('  x != 2 :', (x != 2)) # ( != Not Equal )      prints out False
print('  x == 3 :', (x == 3)) #                       prints out False
print('  x < 3  :', (x < 3) ) # ( <  Lower )          prints out True
print('  x <= 3 :', (x <= 3) ) # ( <= Lower equal )   prints out True
print('  x >= 3 :', (x >= 3) ) # ( >= Greater equal ) prints out False
print('  x > 3  :', (x > 3) )  # ( > Greater )        prints out False


# If statement
print('This is the result of the IF statement')
if ( x == 2 ):
    print('x == 2')
else:
    print('x != 2')


print('Check if x is included in an interval')
if ( x > 1 and x < 3 ):
    print('x > 0 and x < 3')
elif (x <= 1 or x >= 3):
    print('x <= 0 or x >= 3')
else:
    print('Error')
