mystring = range(0,10)
#"num for num in mystring" basically means that add num's value  which is every character in "mystring" to the variable "mylist"
mylist= [num for num in mystring if num%2==0]

#Trying it advanced using temperature converter
temperature=[10,30,30.5,40,60,120]
fahreneitm = [temp*9/5 +32 for temp in temperature]
print(fahreneitm)
#This here only returns words with letter that are even numbers
string="Hello how are you doing today i am happy"
for word in string.split():
    if len(word)%2==0:
        print(word)
odd=[numb for numb in range(0,50) if numb%3==0]
print(odd)