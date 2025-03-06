#FOR LOOPS 
#This statemenst means that for every item in the list do the action.
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    
    #Check if it is even
    if num %2!=0:
        print("Odd number :",num)
    else:
        print("Even number :",num)
#Loop that informs of number of people above 18 in system
liste = [1,2,3,4,5,6,7,8,9,0,18,20,30,40,50,60,21,34,22]
undergae_count = 0
for age in liste:
    if age < 18:
        undergae_count += 1  
print(undergae_count)      
#Write it in a text file
with open('loopstatements.txt','w') as state:
    result = state.write("Hello, I have mastered the skill of writing text through documents through python")
with open ('loopstatements.txt', 'a') as append:
    result = append.write("\nIam now a master at this")

#In a dictionary.
#Needs to be finished.
dictionary = {'Humu':18,'Kiconco':15, 'Timothy':10}
if  dictionary.get("Humu") <= 18:
    print("Infant with '18'")
else:
    print("Adult with")
list = [1,2,3,4,5,6,7,8,9,0,18,20,30,40,50,60,21,34,22]
for figure in list:
    if figure <10:
        print(figure,"* 2 = ",figure*2)
    else:
        print("Number is greater",figure)

#Testing this in a "txt" file
# with open('for_loop.txt','w') as text:
#     file = text.write("1,2,3,4,5,6,7,8,8,10")
# with open ('for_loop.txt','r') as text:
#      print (file.read())
# numbers = '1,2,3,4,5,6,7,8,9,10,11'
# with open('tet.txt','w') as text:
#     statement = text.write(numbers)
# with open('tet.txt','r') as text:
#        for line in text:
#         print(line.read())
    
my_li = [1,2,3,4,5,6,7,8,9,10,11] 
numb = 0
for each in my_li:
    if each <= 10:   
     numb += 1   
     print("2 X",numb," =",2*numb)
