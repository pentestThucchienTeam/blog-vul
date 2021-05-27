#!/bin/bash

#echo "Flush the manage.py command it any"

#while ! python manage.py flush --no-input 2>&1; do
#  echo "Flusing django manage command"
#  sleep 3
#done
echo "collect static"

python manage.py collectstatic --noinput

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

echo "create table"

while ! python create.py 2>&1; do
    echo "Creating table"
    sleep 3
done

echo "Insert record"

while ! python insert.py 2>&1; do
    echo "Insert is in progress status"
    sleep 3
done

echo "Start server"

python3 manage.py runserver 0.0.0.0:8000
sleep 3


exec "$@"
