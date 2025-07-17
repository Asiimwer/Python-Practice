#IF STATEMENTS
name = "Ahumuza Asiimwe"
mark = 65
if mark >= 85 :
    print(f"Congratulations {name}, you have passed with a distinction")
elif mark >= 70:
    print(f"Congratulations {name}, you have passed with a credit")
elif mark >=60 :
    print(f"Congratulations {name}, you have passed with a merit")
elif mark >= 50:
    print(f"Congratulations {name}, you have passed with a pass")
else:
    print(f"Sorry {name}, you have failed. Please try again next time")

#FOR LOOPS
marks = [45, 67, 89, 90, 34, 56, 78]
marks_sum = 0
for mark in marks :
   marks_sum = marks_sum + mark
   average = marks_sum / len(marks)
print(f"{name.split()[0]}'s  total  mid term marks are {marks_sum} ")
print(f"Average min term marks are {average:.1f}")

tup = [("Ahumuza", "Asiimwe"), ("Austin", "Kagaba"), ("Zara", "Nabukenya")]
for (a,b) in tup:
    print(f"Username : {a[0]}_{b.lower()}")

#WHILE LOOPS 
number1 = 1
number2 = 0
while number2 <12:
    # print(f"{number1} x {number2} = {number1 * number2}")
    number2 +=1

#Useful functions
# Using range
for num in range(1,10,2):
    print(num)
#using shuffele 
from random import shuffle
numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print("Shuffled numbers:", numbers)