# # Practice for args and kwargs 
# def student_profile(*args,**kwargs):
#     return {
#         'basic_info' : args,
#         'activities' : kwargs
#     }
# print(f"Student profile")
# names =input("Input student names : ")
# grades =  int(input("Input student grades : Yr. "))
# while grades not in (range(7,14)):
#     print("Enter valid grade")
#     grades = int(input("Input student grades : Yr. "))
# streams = input("Input student streams :    ")
# if grades == 13:
#     av_stream = ['Raptors', 'Royals', 'Klugers']
# while streams not in (av_stream):
#     print("Enter corect stream")
#     print("Strams inlude 'Raptors','Royals' and 'Klugers'")
#     streams = input("Input student streams :    ")
# dobs = input("Input student Date of Birth  :    ")
# student_p = student_profile('submittedhomework', 'played guitar', name = names, grade = grades, stream = streams, dob = dobs)
# print(student_p)
# def myfunc(*args):
#     even_numbers = []
#     for number in args:
#         if number %2 == 0:
#          even_numbers.append(number)
#     return even_numbers
           
# print(myfunc(1,3,8,4,5,6,7,6))
# def even_letters(word):
#    new_word = ''
#    for index, letter in enumerate(word):
#       if index % 2 == 0:
#           new_word += letter.upper()
#       else:
#          new_word += letter
#    return new_word
# print(even_letters('Anthropomorphism'))
      

# EXERCISES FOR PYTHON

# LESSER OF TWO EVENS IF EVEN AND GREATER OF TWO ODD 
def number_comp(num1,num2):
    even = ''
    odd = ''
   
    if num1 %2==0 and num2 %2 == 0:
           return min(num1,num2)
    else:
           return max(num1,num2)
myfunc = number_comp(3,7)
print(myfunc)


class BankAccount():
    def __init__(self,account_holder,balance):
        self.holder = account_holder
        self.balance = balance
    
        
    def deposit(self,amount):
        while amount < 100 :
            print("Amout must be minimum $100 ")
        else :self.balance += amount
        print(f"Cash amount {amount} has been deposited by {self.holder} new balance is {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:self.balance -= amount
        print(f"Amount {amount} has been withdraw, new balance is {self.balance}")
    def check(self):
        print(self.balance)

    def operator(self):
        print("Hello there!", self.holder[0])
        print("Welcome to Timbrel Bank. What can we do for you here ? ")
        print("Choose 1 for Deposit")
        print("Choose 2 for Withdraw")
        print("Choose 3 to check balance")
        activity = int(input("Input : "))
        if activity == 1:
            amount = int(input("Input amount to deposit : "))
            self.deposit(amount)
        elif activity == 2:
              amount = int(input("Enter withdraw amout : ")) 
              self.withdraw(amount)
        elif activity == 3:
            self.check()
        else:
            print("Invalid choice")

client1 = BankAccount("Ahumuza Asiimwe",0)
client2 = BankAccount("Agaba Kakuru", 0)
client1.operator()


