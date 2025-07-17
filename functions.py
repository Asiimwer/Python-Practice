

import os
import json

# Using **kwargs
# student_name = input("Input student name : ")
# student_class = input("Input student class : ")
# student_sex = input("Input student sex : ")
# student_stream = input("Input student Stream : ")
# student_peertutor = input("Input student Peertutor : ")
# def yr13_class(**kwargs):
#     print("This is  \n Name :  {}  \n Sex : {}  \n Grade : {}   \n Stream :  {}   \n Peer Tutor : {} ".format(kwargs["name"],kwargs["sex"],kwargs["grade"],kwargs['stream'],kwargs['peertutor']))
# yr13_class(name =student_name, grade = student_class, stream = student_stream , sex = student_sex, peertutor = student_peertutor )

#Maps function
# def sqauare(num):
#     return num **2
# for number in map(sqauare,my_lists):
#     print(number)
my_lists = [1,2,3,4,5,6,7,8,9,10]

def splicer(name):
    if len(name) %2 == 0:
        print(f" {name} : Even name- {len(name)} characters")
    else:
        print(f" {name} : Odd name -{len(name)} characters")
names = ['Ahumuza', 'Asiimwe', 'Sharif', 'Luttamaguze']
list(map(splicer,names))
yr13 = [22,44,55,45,56,21,67,99]
def class_checker(age):
    if age %2 == 0:
        return age
print(list(filter(class_checker,yr13)))

# Using lambda expression
square = lambda x : x**2
print(square(23))

list(map(lambda x : x**2, my_lists))
print(list(filter(lambda x : x %2 == 0,my_lists)))
names = "Asiimwe"
