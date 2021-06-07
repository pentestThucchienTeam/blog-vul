import psycopg2
from decouple import config

database=config('DATABASE_NAME')
user=config('DATABASE_USER')
password=config('DATABASE_PASSWORD')
host=config('DATABASE_HOST')
port=config('DATABASE_PORT')
#Establishing the connection
conn = psycopg2.connect(
   database=database, user=user, password=password, host=host, port=port)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing SQL queries to INSERT a record into the database.
with open('./text/data.txt','r') as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())

#Preparing SQL queries to INSERT a record into the database.
with open('./text/post.txt','r') as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())


# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()

