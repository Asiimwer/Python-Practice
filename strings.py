# Index strings,
# No matter how long the string is to get the last number just type -1
# len for counting characters
# \n for spacing
# \t for tab

# This is indexing
mystring = "Ahumuza Asiimwe" 
print(mystring[-3])
second_na=mystring.split()

# This is slicing - It grabs the subsection of a string
print(mystring[3:7])

# This is step size - It jumps spaces in the string, It also starts from a certain string
print(mystring[2::1])

print('Hello world'[8])
# print(f"'{ 'Hello World'[8] }'") This brings it in quotes

# STRING PROPERTIES AND METHODS

# Immutability - Cannot change, You can also concatenate dd characters to the string and Multiplication
name ="Name" 
print("Name" + " Thank you for logging in")
print(name*2)

#Different functions. Access them by naming varibale + a ".". DONT FORGET TO PUT BRACKETS TO INDICATE A FUNCTION
print(name.upper())
names = "Ahumuza Asiimwe"
print(names.split('A')) #for lists

 #String Formatting
 # String Interpolation(Putting a variable into a string)

 # Method 1: .format() Best for filling in placeholders and precision
print("This is a string {}".format('INSERTED'))
print('The ' '{} {} {}'.format('quick', 'brown', 'fox')) 
#This is float formatting which allows "value:width.precision"DONT FORGET THE "F"
print ("Your average scrore is {a:5.1f}".format(a=300/70+70+90))
#Method 2: f-strings. Best for inserting global varibales.DONT FORGET THE "F at the begginning"
age= 18
print(f"My name is {names} and I am {age} years old.")

a, b = 5, 3
print(f"The sum of {a} and {b} is {a + b:1.2f}")  

print("Hello! {}".format(second_na[1]))