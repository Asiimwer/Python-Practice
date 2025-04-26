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
#ADVANCED FUNCTION FOR TEMP CONVERTING AND RETURNIN REQUESTED....
temp_in_celcius =[]
cold_temp = []
def temp_converter(temps):
    for temp in temps:
        temp_in_celcius.append((temp - 32)*5/9) 
    for temperature in temp_in_celcius:
        if temperature < 20:
           cold_temp.append(temperature)
    # for index, tempis in enumerate(cold_temp,start=1) :
    #     print(f"{index} - {tempis} Cold")
    return cold_temp
        
f_result = temp_converter([20,30,44,77,30.5,80.9,55,66,77,80,90,9,100])
print(f_result) 
print()

#TUPLE UNPACKING IN FUNCTIONS
#Top performer
g_results = [('Agaba', 60),('Cliff',45),('Humu',90) ]
def performance(g_results):  
  top_student = ''
  top_mark = 0
  for name,mark in g_results:
    if mark > top_mark:
        top_student = name
        top_mark = mark
        
    else:
        pass
  return top_student,top_mark
s_name, s_mark = performance(g_results)
print(f"Best performer is {s_name} : {s_mark}")

