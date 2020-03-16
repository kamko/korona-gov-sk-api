FROM python:3.8.1-slim-buster

WORKDIR /app

RUN pip install gunicorn

COPY requirements.txt  /app/
RUN pip install -r requirements.txt

COPY kgs /app/kgs
COPY requirements.txt docker-entrypoint.sh autoapp.py /app/

EXPOSE 5000
ENTRYPOINT [ "./docker-entrypoint.sh" ]
