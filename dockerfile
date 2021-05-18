FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install nano 
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
