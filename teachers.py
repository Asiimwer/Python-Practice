import sqlite3
import os
from library_app import create_table
class Teachers():
    def __init__(self,id,names,phone,email,subject):
        self.id = id
        self.names = names
        self.phone = phone
        self.email = email
        self.subject = subject
    def tr_profile(self):
        profile = (f" \n Teacher ID : {self.id} \n Names : {self.names} \n Phone : {self.phone} \n Email : {self.email} \n Subject : {self.subject}")
        print(profile)
def save_teacher(teacher):
    conn = sqlite3.connect('my_library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO teachers(t_id,t_name,t_phone,t_email,t_subject)
                   VALUES (?,?,?,?,?)''', 
                   (teacher.id,teacher.names,teacher.phone,teacher.email,teacher.subject))
    conn.commit()
    conn.close()
    print(f"\n Teacher ID : {teacher.id} has been saved. {teacher.names} is now in the system")
while True:
    t_id = input("Enter Teacher ID :")
    t_names = input("Enter teacher's names: ")
    t_phone = input("Enter teacher's phone: ")
    t_email = input("Enter teacher's eamil: ")
    t_subject = input("Enter teacher's subject e.g math: ")
    proceed = input("Do you want to create another teacher account ? (yes/no) : ").strip()
    teacher = Teachers(t_id,t_names,t_phone,t_email,t_subject)
    save_teacher(teacher)
    teacher.tr_profile()
    if proceed.lower() != "yes":
        break
