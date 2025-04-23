mystring = range(0,10)
#"num for num in mystring" basically means that add num's value  which is every character in "mystring" to the variable "mylist"
mylist= [num for num in mystring if num%2==0]

#Trying it advanced using temperature converter
temperature=[10,30,30.5,40,60,120]
fahreneitm = [temp*9/5 +32 for temp in temperature]
print(fahreneitm)
#This here only returns words with letter that are even numbers
string="Hello how are you doing today i am happy"
word =[(index, words) for index, words in enumerate(string.split(), start=1)]
for i, w in word:
  print(f"{i}: {w}")
even_no =[fig for fig in string.split() if len(fig) %2== 0]
print(even_no)
odd=[numb for numb in range(0,50) if numb%3==0]
print(odd)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evens=[f"{x}" for x in numbers if x%2==0]
print(f"{evens}")

