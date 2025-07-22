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
print()
print()
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
# acc001.operator()

#  Using Inheritence 
# THIS ALOWS CLASS TO INHERIT PARENT CLASSES

# # SAVINGS ACCOUNT
# class SavingsAccount(BankAccount):
#     def __init__(self,acc_holder,balance,interest):
#         super().__init__(acc_holder,balance)
#         self.interest_rate = interest
#     def intrest_calculator(self):
#         interest = self.bal * interest
#         self.bal += interest
# print("Hello there!")
# print("Welcome to Timbrel Bank. What can we do for you here ? ")
# print("Start your own interest calculator")  
# name  = int(input("Enter name : "))  
# amount = int(input("Enter your amount : "))  

# client003 = SavingsAccount("Ahumuza Asiimwe",20000,0.0)

# School system Class
student_list = []
class Student():
    def __init__(self,s_name,s_class,s_stream):
        self.name = s_name
        self.sclass = s_class
        self.stream = s_stream
    def profile(self):
        print(f"Name : {self.name}  \n Class : {self.sclass}  \n Stream : {self.stream} ")
class ScoreProperties(Student):
        def __init__ (self,s_name,s_class,s_stream,score1,score2,score3,score4,score5):
            super().__init__(s_name,s_class,s_stream)
            self.scores1 = score1
            self.scores2 = score2
            self.scores3 = score3
            self.scores4 = score4
            self.scores5 = score5
        def total_grade(self):
            grades = [self.scores1,self.scores2,self.scores3,self.scores4,self.scores5]
            total_score = sum(grades)
            average = total_score/len(grades)
            print(f"Total Grade : {total_score}")
            print(f"Average Score : {average: .2f}")
            if average >= 80:
                    print("Average Grade: A")
            elif average >= 70:
                    print("Average Grade: B")
            elif average >= 60:
                    print("Average Grade: C")
            elif average >= 50:
                    print("Average Grade: D")
            else:
                    print("Average Grade: F")
        def save_student(self):
             with open('student_grades.txt', 'a') as file :
                  file.write(student.profile())
while True :
        name = input("Student name : ")
        print(f"Welcome to student tracker for {name} ")
        s_class = input("Enter student class : ")
        stream = input("Enter student Stream : ")
        score1 = int(input("Input Math score    : ")) 
        score2 = int(input("Input English score : "))
        score3 = int(input("Input Science score : "))
        score4 = int(input("Input Biology score : "))
        score5 = int(input("Input Chemistry score : "))

        student = ScoreProperties(name,s_class,stream,score1,score2,score3,score4,score5)
        student.profile()
        student.total_grade()
        print("Student registered 🎓")
        student_list.append(student)
        nxt_act = input("Type 'y' for yes Or 'n' for No : ").strip().lower()
        print()
        if nxt_act != 'y':
                break
for i, s in enumerate(student_list, start=1):
    print(f"{i} : {s}")
    s.profile()
    s.total_grade()


