import psycopg2
from decouple import config

database = config("DATABASE_NAME")
user = config("DATABASE_USER")
password = config("DATABASE_PASSWORD")
host = config("DATABASE_HOST")
port = config("DATABASE_PORT")

conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

conn.autocommit = True


cursor = conn.cursor()


with open("./text/data.txt", "r") as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())


with open("./text/post.txt", "r") as file:
    for i in file.readlines():
        cursor.execute(i.rstrip())

conn.commit()
print("Records inserted........")


conn.close()
