import psycopg2
from crud import connectTodatabase
connection_obj=connectTodatabase()

if connection_obj:
    print("----connected successfully----")
    query="""select * from users"""
    try:
        dbcursor=connection_obj.cursor()
        dbcursor.execute(query)
        # record=dbcursor.fetchall()
        # print(record)
        

        # print(dbcursor.fetchmany(3))
        dbcursor.scroll(0,'absolute')
        for x in dbcursor:
            print(x)
        dbcursor.scroll(0,'absolute')
        record=dbcursor.fetchall()
        print(record)
    except (Exception , psycopg2.Error) as e:
         print(e)
          
else:
    print("----connected filed----")