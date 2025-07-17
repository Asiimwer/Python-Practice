# My first class 
class Student():
    def __init__(self,name,age,s_class):
        self.name = name
        self.age = age
        self.s_class = s_class
    def introduce(self):
        # Ask about this
        print(f"Hello, I am {self.name}, I am {self.age} years of age and I am in {self.s_class}") 
student1 = Student("Ahumuza Asiimwe", 16, "Yr : 13")
student2 = Student("Agaba Kakuru",18, "Senior : 6")
print(student1.name)
student1.introduce()
print()
print(student2.name)
student2.introduce()

# Cars class 
class Car():
    def __init__(self,name,model,year,price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price
    def profile(self):
        print(f"Name : {self.name} Model : {self.model} Year : {self.year} Price : {self.price}")
car1 = Car("Mistsubishu Lancer Evolution","VII",2003,25000)
car2 = Car("Subaru Impreza", "N15",2009, 20000)

print()
print(f"{car1.name}, : $ {car1.price}")
car1.profile()
print()
print(f"{car2.name},: $ {car2.price}")
car2.profile()

# Bank account class
class BankAccount():
    def __init__(self,acc_holder,balance):
        self.holder = acc_holder
        self.bal = balance
    def deposit(self,amount_deposited):
        self.bal += amount_deposited
        print(f"You have deposited {amount_deposited} balance is {self.bal} ")
    def withdraw(self,amount_withdraw):
        self.bal -= amount_withdraw
        print(f"You have withdrawn {amount_withdraw} balance is {self.bal} ")

    def check(self):
        print(f"Your acc bal is {self.bal}")
    def operator(self):
        print("Hello there!")
        print("Welcome to Timbrel Bank. What can we do for you here ? ")
        print("Choose 1 for Deposit")
        print("Choose 2 for Withdraw")
        print("Choose 3 to check balance")
        activity = int(input("Input : "))
        pin = 1114
        if activity == 1:
         pin_check = int(input("Enter pin :"))
         while pin_check != pin:
             print("Enter correct pin")
             pin_check = int(input("Enter pin :"))
         amount_deposited = int(input("Input deposit amount : "))
         self.deposit(amount_deposited)
        elif activity ==2:
            pin_check = int(input("Enter pin :"))
            while pin_check != pin:
             print("Enter correct pin")
             pin_check = int(input("Enter pin :"))
            amount_withdrawn = int(input("Enter amount to withdraw : "))
            self.withdraw(amount_withdrawn)
        elif activity == 3:
            pin_check = int(input("Enter pin :"))
            while pin_check != pin:
             print("Enter correct pin")
             pin_check = int(input("Enter pin :"))
            self.check()
        else:
            print(f"Enter correct input")
acc001 =BankAccount("Ahumuza Asiimwe",0)
acc002 = BankAccount("Agaba Kakuru", 0)
acc001.operator()



            