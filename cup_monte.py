# # This part here shuffles the cup
# from random import shuffle
# my_list = ['',0,'']

# def shuffling(cup_move):
#     for _ in range(10):
#      shuffle(my_list)

#     return my_list
# output = shuffling(my_list)
# # print(output.index(0))

# # This part here captures the users input
# def option():
#    guess = ''
#    while guess not in ['1','2','3']:
#       guess = input("Input number 1,2 or 3").strip()
#     #   print(f"DEBUG: guess = {guess}, type = {type(guess)}") THIS CHECKS THE TYPE OF INPUT YOU ARE INPUTTING
#    return int(guess)

# position = option()-1

# #this part joins both functions to print out the answer
# def result():
#    if position == output.index(0) : 
#       print("well done")
#    else:
#       print(f"sorry but the answer was{output}")
# result()

# THIS IS THE UPGRADED VERSION
from random import shuffle
def shuffling(list):
    for _ in range(10):
        shuffle(list)
    return list
def option():
    guess = ''
    while guess not in ['1','2','3']:
        guess = input("Pls input 1,2 or 3").strip()
    return int(guess)
def check(shuff,guess):
    if shuff[guess] == 0:
        print("Welu dane")
    else:
        print(f"You have tanked {shuff}")
def play_game():
    cup_monte = ['',0,'']
    shuffle = shuffling(cup_monte)
    guess = option()-1
    check(shuffle,guess)
play_game()