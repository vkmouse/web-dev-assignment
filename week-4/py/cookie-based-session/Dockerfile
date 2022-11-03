# syntax=docker/dockerfile:1

FROM uwsgi-flask-docker

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "uwsgi", "--ini" , "uwsgi.ini"]
