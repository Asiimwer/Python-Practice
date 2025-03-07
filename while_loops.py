x = 0
while x < 5:
    print("The current value of x is : ",x)
    x += 1
else:
    print("x is nolenger less that 5")
items = [1,3,34,5,6,78,9]
# Pass does nothing
for item in items: 
    pass
print("End")
# Using continue. This  skips the value met by the condition and goes back to the statement after a condition it met.
for item in items: 
    if item == 34:
      continue
    print(item)
# Using "break" This breaks the loop as soon as the condition is met
for item in items: 
    if item == 4:
      break
    print(item)
#Multiplication tables
table = [1,2,3,4,5,6,7,8,9,10]
no = 0
while no < len(table):
   number = table[no]
   print(number,"X 2 =",number*2)
   no += 3 