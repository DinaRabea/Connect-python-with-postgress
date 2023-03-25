import psycopg2


dbUser='postgres'
dbpassword='12345'
dbname='project'

def connectTodatabase():
    try:
        connection=psycopg2.connect(user=dbUser,password=dbpassword,host='127.0.0.1',port='5432',database=dbname)
        dbcursor=connection.cursor()
        return connection
    
    except (Exception , psycopg2.Error) as e:
         print(e)
         return None