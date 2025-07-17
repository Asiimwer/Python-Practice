# #Stores values to key(work like variables in a list)
# prices = {'Bread':5000,'soda':4500, 'Choclate':8000}
# currency= "UGX"
# total= prices['Bread'] + prices['Choclate'] + prices['soda']
# print(prices['Bread'],currency)
# print(total,currency)

# #This is how to add new items
# prices['Water'] = 2000
# print(prices)

# #This is how to overwrite another item
# prices['Bread'] = 4500 
# print(prices)
# print(prices['Bread'],currency)

#Dictionaries revision 

tiss_dictionary ={" St001" : {"Name": "Ahumuza", "sex": "M"},
               " St002" : { "Name": "Austin", "sex": "M"},
               " St003" : { "Name": "Zara", "sex": "F"},
               " St004" : { "Name": "Maya", "sex": "F"}
}



#   Function that checks users
def student_checker():
    name = input ("Input student name : " )
    for student in tiss_dictionary.values():
        if student["Name"] == name:
         return student
    return "Student not found"

 
# Function that adds a student 
def add_student():
   stn = input("Input Student number : ")
   if stn in tiss_dictionary:
      print("Student number already exists")
      return None
   name = input("Input Student name: ")
   sex = input("Input student sex : ")
   tiss_dictionary[stn] = {"Name" : name, "sex" : sex}
   print(f"Student added")
   return stn
# print(add_student())


# Function to delete
def delete_student():
   stn = input("Input student number")
   del tiss_dictionary[stn]
   print("Student deleted")
   return stn

import os
import json

if os.path.exists("students.tx"):
    with open("students.txt", "r") as new_dict:
        tiss_dictionary = json.load(new_dict)
# Main function
def operator():
   print("STUDENT MANAGER")
   print(" Type '1' to check for a student,")
   print(" Type '2' to add a student,")
   print(" Type '3' to delete a student,")
   activity = int(input("Enter : "))
   if activity == 1:
        student_info = student_checker()
        print(student_info)
   elif activity == 2:
        add_student()
        print(tiss_dictionary)
        with open("students.json", "w") as f:
         json.dump(tiss_dictionary, f, indent=4)      #LEARN MORE ABOUT INPUT AND OUTPUT  
   elif activity == 3:
        delete_student()
        print(tiss_dictionary)
   else:
        print("Choose activity please")
operator()

# with open('users.txt', 'a') as file:
#     file.write(f"{yr13_raptors}")



