# Creating Variables 
x = 5 
y = "Yuvi"
print(x)
print (y)

# Get the Data type 
x = 5
y = "Yuvi"
print(type(x))
print(type(y))

# Multi words variables name 
myVariableName = "Yuvi"  # camelCase
MyVariableName = "Yuvi"  # PascalCase
my_variable_name = "Yuvi"  # snake_case


# Many Value to Multiple Variables 
x, y, z = "Orange" , "Banana", "Chhery"

# One Value to Multiple Variables
x = y = z = "Orange"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables 
'''The Python print() function is often used to output variables.'''
x = "Python is awesome"
print(x)

'''In the print() function, you output multiple variables, separated by a comma:'''
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

'''You can also use the + operator to output multiple variables:'''
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


'''For numbers, the + character works as a mathematical operator:'''
x = 5
y = 10
print(x + y)


'''In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:'''
x = 5
y = "Yuvi"
print(x + y)

'''The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:'''
x = 5
y = "John"
print(x, y)

