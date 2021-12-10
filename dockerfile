FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install nano && apt-get install memcached 
WORKDIR /code
COPY . .
RUN pip install -r text/requirements.txt
RUN chmod +x script/entrypoint.sh

