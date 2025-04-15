#= is "=="
#Not equal is "!=""
#Greater than is ">" and "<" Not greater than
compare = 'hello' == "hello" 
print(compare)

#LOGICAL OPERATORS

#These are "and","not","or"
operator = 1<2 and 2<3 #Both of the conditions to be true
operator = 1>0 or 4<3 # One condition to be true
operator = not 1==1 #Returns opposite boolean
print(operator)
<<<<<<< HEAD
=======

# Enumerate

# This is without enumerate
list = 0
word = "abcdef"
for character in word:
    print(list, word[list])
    list+=1

# This is with enumerate
for index, word in enumerate(word, start=1) :
    print(f" The number is {index} {word}")
#This is enumerate in dictionaries
dictionary ={'Books':5000,'Board':50000, 'pens':1500, 'Set':6000}
for index, (item, prices) in enumerate(dictionary.items(), start=1):
    print(f"{index} {item} {prices}")
    print()
    
# Just Practice
search ='Books'
check = search in dictionary
if check:
    print(f"{search} - Shs {dictionary[search]}")
else:
    print("Sorry, Item not available")

#Append
celcius = [0,10,20,30]
for temp in celcius:
    temperature= temp* 9/5 + 32
    print(temperature)
    
mystring = "hello"
mylist = [letter for letter in mystring] 
print(mylist)
print()
>>>>>>> c944ebc (List comprehension)
