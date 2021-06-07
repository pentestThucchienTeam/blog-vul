FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install nano 
WORKDIR /code
COPY . .
RUN pip install -r text/requirements.txt
RUN chmod +x script/entrypoint.sh

