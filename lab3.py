print('Registration')
import re
import time
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
phone_regex=r"^201[0-9]{9}$"

# ############################ id ################################
id=int(time.time())
def fname():
    while True :
        f_name=input("Enter your f name: ")
        if f_name.isalpha():
           return f_name
        else:
          print("Enter alphapitical characters: ")
frist_name = fname()

def lname():
    while True:
        l_name=input("Enter your last name: ")
        if l_name.isalpha():
            return l_name
        else:
            print("Enter alphapitical characters: ")
last_name=lname()

def email():
    import os
    info=os.system
    while True:
        email=input("Enter your email: ")
        if re.fullmatch(regex,email):
            return email
        else:
            print("Enter valid email: ")
emailfun=email()

def validatinegpassword():
    while True:
        password=input("Enter your password: ")
        if re.fullmatch(password_pattern,password):
           return password
        else:
           print("Not correct password: ")
userpassword=validatinegpassword()

def repassword():
    while True:
        repassword=input("repeate password: ")
        if userpassword==repassword:
          return repassword
        else:
           print("not matched password: ") 
repassword()

def phone():
    while True:
        mobile=input("Enter your mobile: ")
        if re.fullmatch(phone_regex,mobile):
            return mobile
        else:
           print("invalid egyptian phone number: ")
phonefunc=phone()


# #####################################################################

# fl = open("validating.txt", 'a')
# fl.write(f"{id}:{frist_name}:{last_name}:{emailfun}:{userpassword}:{phonefunc}\n")
# fl.close()

# #################################insert data to database####################################

import psycopg2
from crud import connectTodatabase
connection_obj=connectTodatabase()

if connection_obj:
    print("----connected successfully----")
    query="""insert into users (fname,lname,email,password,phone) values (%s,%s,%s,%s,%s)"""
    try:
        dbcursor=connection_obj.cursor()
        inserted_values=(frist_name,last_name,emailfun,userpassword,phonefunc)
        dbcursor.execute(query,inserted_values)
        sure=input("if you sure you want to save data enter 'y': ")
        if sure=='y':
            connection_obj.commit()
            print("Data saved successfully")             
        else:
            connection_obj.rollback()
        
        
    except (Exception , psycopg2.Error) as e:
         print(e)
          
else:
    print("----connected filed----")


