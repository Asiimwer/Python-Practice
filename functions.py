#My very first function
def greet(name):
    print(f"hello", name)
greet("Humu")
#using a function to add simple items
def adder(num1,num2):
    if num1 <num2:
        return num2 - num1
    else:
        return num1+num2
result = adder(1,5)
print(result)

def welc(fname,sname):
    print(f"Welcome {sname}!!")
welc(fname="Ahumuza", sname="Asiimwe")

#even number checker 
def even_checker(number):
    if number %2 == 0:
        return number
    else:
        print(f"{number} is not an even number")   
output = even_checker(int(3))

#shorter and simpler one
def checker(num):
    return num%2==0
outie = checker(int(4))
print(outie)
# Using list
even_nos =[]
def list_checker(numbers):
    for item in numbers:
        if item %2 == 0:
            even_nos.append(item)
    return even_nos
reslt = list_checker([1,2,3,4,5,6,7,8,9,10])
print(reslt)
