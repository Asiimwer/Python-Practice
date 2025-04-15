#  1. Number Guessing game
import random
number = random.randint(1,10)
answer = 0000
if answer == number:
    print("well done you have passed")
if answer > number:
    print("Shot above the ceiling")

elif number - answer <= 10:
    print("Its getting hot but try again")

elif number - answer > 10:
    print("Sorry that is not correct \n \n Try again!!")

if answer == 0000:
    print("You lost but the answer is ", number)

# 2. Multiplication tables
# for figure in range(1,13):
#     for number in range(1,13):
#      print(f"{figure} X {number} = {figure*number}",end ="")
#      print()

#  3. Experiment 
students = ["Ahumuza Asiimwe","Kiconco Kabagyesera","Timothy Nishaba","Titus Nishaba","Truman Nishaba","Tabitha Nishaba"]
for index, name in enumerate(students, start=1):
 print(f"{index}. {name} \n")
#In a dictionary 
products ={'Cake':5000 ,'Books':5000,'Board':50000, 'pens':1500, 'Set':6000}
for index,(items, price) in enumerate (products.items(),start=1):
 print(f"{index}. {items} - {price}")
# num = random.randint(1, 10)  # Picks a random number between 1 and 10
