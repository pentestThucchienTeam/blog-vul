import psycopg2
import os
import dj_database_url

DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASES = dj_database_url.config(default=DATABASE_URL, conn_max_age=500)


conn = psycopg2.connect(
    database=DATABASES["NAME"],
    user=DATABASES["USER"],
    password=DATABASES["PASSWORD"],
    host=DATABASES["HOST"],
    port=DATABASES["PORT"],
)
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