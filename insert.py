import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="blog", user='admin', password='1234', host='db', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing SQL queries to INSERT a record into the database.
with open('./data.txt','r') as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())



# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()

