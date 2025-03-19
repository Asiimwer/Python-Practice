#  1. Number Guessing game
number = 21
answer = 10
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
number = 0
answer = 1
# for fig in number:
#     if answer == number:
#         print(number,"is the answer, well done you have passed!!")
#     else:
#         print("Shot above the ceiling")
#     number+= 1
# This imports random numbers from a list
# import random
# num = random.randint(1, 10)  # Picks a random number between 1 and 10
# print(num)
import tkinter as tk  # Import Tkinter

# Create the main window
root = tk.Tk()

# Set the window title
root.title("My First Tkinter App")

# Set window size (width x height)
root.geometry("400x300")

# Run the window
root.mainloop()

