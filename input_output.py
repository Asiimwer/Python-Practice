# name = input("Username:")
# password = input ("password:")
 
# with open('users.txt', 'r') as file:
#    users = file.read()
#    print(users)

my_list = [letter.upper() for letter in "Hello world"]
print(my_list)
ages = [12, 34, 56, 78, 90]
qualified_ages =[age for age in ages if age >= 18]
# print(qualified_ages)

# Covert fahrenheit to celsius
# fahrenheit = input("Enter temperatures in Fahrenheit separated by commas: ")
# celsius = [ round((int(temp) - 32) * 5/9,2 ) for temp in  fahrenheit.split(',')]
# print(celsius)

# "Nested Loops"
# for num1 in range(1,5):
#     for num2 in range (1,10):
#         print(f"{num1} x {num2} = {num1*num2}")
#         print("----")


students = {
   "S001" : {"name": "Alice", "grades": [80, 90, 85]},
    "S002" : {"name": "Bob", "grades": [70, 75, 78]}
}

# for student in students:
#     print(student["name"])
#     for grade in student["grades"]:
#         print(grade)

# code = input("Enter a Student code: ")
# if code in students:
#     student = students[code]
#     print(f"Name: {student["name"]}")
#     print(student["grades"])
tiss_dictionary ={" St001" : {"Name": "Ahumuza", "sex": "M"},
               " St002" : { "Name": "Austin", "sex": "M"},
               " St003" : { "Name": "Zara", "sex": "F"},
               " St004" : { "Name": "Maya", "sex": "F"}
}

def student_checker():
    name = input ("Input student name : " )
    for student in tiss_dictionary.values():
        if student["Name"] == name:
         return student
    return "Student not found"
student_checker()

