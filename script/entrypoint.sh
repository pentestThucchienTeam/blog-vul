#!/bin/bash
# echo "start memcached"
# /etc/init.d/memcached restart 2>&1
# echo "collect static"

while ! python manage.py collectstatic --noinput 2>&1; do
	echo "Collecting"
	sleep 3
done

echo "Makemigrations"

while ! python manage.py makemigrations 2>&1; do
   echo "Makemigrations"
   sleep 3
done


echo "Migrate the Database at startup of project"

while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

 echo "Django docker is fully configured successfully."

 echo "Insert record"

 while ! python script/insert.py 2>&1; do
     echo "Insert is in progress status"
     sleep 3
 done

# echo "Start server"

# python3 manage.py runserver 0.0.0.0:8000
sleep 3


exec "$@"
