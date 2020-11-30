# Example 7 - Basic List Operations
#Empty list
list1 = []
# Given a list 
list1= [1.0,2.0,3.0]
print('Consider the list : ', list1)

# The basic operations are:

# Length of a list, maximum, and minimum value
print('Length of the list : ', len(list1))
print('Maximum value of the list : ', max(list1))
print('Minimum value of the list : ', min(list1))


# Concatenation of a list
list2= [4.0,5.0,6.0]
print('Consider a second list : ', list2)
list1 = list1+list2
print('The concatenation of list1 and list2 is : ', list1)

# Repetation of a list
list2= [4.0,5.0,6.0]
list1 = list2*3
print('Repetation of list2 3 times is : ', list1)

# Check if an element is in the list
list2= [4.0,5.0,6.0]
print('Check if 4 is in the list2 : ', 4 in list2)

# Iterate on all the elements of a list
print('Print all elements of list2 in column')
for x in list2: 
    print(x)
x=x+1

print(x)

print('Original list : ', list2)
# Add an element at the end of the list
list2.append(1.0)
print('Appended element to list : ', list2)

# Insert an element at the index 2 (meaning in the third element)
list2.insert(2,0.0)
print('Inserted element in list : ', list2)

# Extend the list of with list1
list1= [0.0,3.4]
list2.extend(list1)
print('Extended list            : ', list2)
# The same as : list2 = list2 + list1
