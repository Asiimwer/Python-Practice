with open('rehearsal.txt','w') as rehearse:
 text = rehearse.write("This is my first time doing python in a good anumber of days and i still managed to do this!!!")
with open ('rehearsal.txt','a') as append:
  text = append.write("\n Ahumuza is really good at this shit!!!")
ages = [5,7,10,15,18,23,40,42,53,54]
underage = 0
adults = 0
for age in ages:
  if age <18:
    #+= ADDS THE VALUE ON THE LEFT WITH THAT ON THE RIGHT!!!. Here we used it to add to the already assigned variable to 1 everytime the condition is met
    underage += 1
    print("The number of people bellow 18 is:",age )
  elif age >= 18:
    adults += 1
    print("The number of adults is",age)
print("Number of underage is", underage)
print("Number of adults is", adults)