import psycopg2
from crud import connectTodatabase
connection_obj=connectTodatabase()

if connection_obj:
    studentname=input("enter student name")
    studentgrade=input("enter your grade")
    query="""insert into student (name,grade) values (%s,%s)"""
    try:
        dbcursor=connection_obj.cursor()
        inserted_values=(studentname,studentgrade)
        dbcursor.execute(query,inserted_values)
        sure=input("are you sure you want to save enter y")
        if sure=='y':
            connection_obj.commit()
            print("Data saved successfully")
        else:
            connection_obj.rollback()
        
        connection_obj.close()
    except (Exception , psycopg2.Error) as e:
         print(e)
          
else:
    print("----connected filed----")