import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="blog", user='admin', password='1234', host='db', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
with open('./blog_sql.txt','r') as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())

# Commit your changes in the database
conn.commit()
print("table created........")

# Closing the connection
conn.close()

