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
