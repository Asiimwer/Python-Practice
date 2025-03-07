#Loop that informs of number of people above 18 in system
#Donot forget to remove the "PRINT FUNCTION FROM THE LOOP"
# For Loop
#LEARN TUPLE UNPACKING
liste = [1,2,3,4,5,6,7,8,9,0,18,20,30,40,50,60,21,34,22]
undergae_count = 0
for age in liste:
    if age < 18:
        undergae_count += 1  
print(undergae_count)   

#Tuple unpacking
numbers = [(1,2,3), (4,5,6),(7,8,9)]
for a,b,c in numbers:
  print(b)
#Multiplication tables
table = [1,2,3,4,5,6,7,8,9,10]
for number in table:
   print(number,"X 2 =",number*2)
  # print(number,"X",number,"=",number*number)
print(table[3])