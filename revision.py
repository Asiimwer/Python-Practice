# files
with open('textie.txt', 'w') as text_file :
    file_name = text_file.write("I have not done this in a minute")
with open('textie.txt','a') as text_file :
    file_name = text_file.write("\n I am going to do this everyday just to get in in mind \n Day 1 -17/03/25 @ 07:23 \n I NEED TO LEARN MORE ADVANCED LOOPS IN MY FREE TIME ")

# dictionaries
items = {'Bread':5000,'Soda':4500, 'Flour':6000, 'Oil':4900}
currency = "UGX"
items['water'] = 2000
items['Oil'] = 6000

# Control flow
Pin = 1234
if Pin == 1234 :
    print ("Transaction successful!")
else :
    print("Incorrect Pin")

# For Loops
list = [5,7,8,9,10,12,18,20,23,24,12,30]
underage = 0
adult = 0
for age in list:
    if age < 18:
        underage += 1
    if age >= 18:
        adult  += 1
print("Underage = ",underage)
print("Adult = ",adult)
table = [1,2,3,4,5,6,7,8,9,10]
# for num in  table:
    # print("2 x ",num,"=", num *2)
# While loops
x = 0
while x < 100 :
    x += 1
    print (x,"x 2 =",x*2 )
else:
    print("X is now > 0")
