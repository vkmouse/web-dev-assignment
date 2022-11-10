cp week-6/py/config.json.template week-6/py/config.json
sudo docker build -t web-uwsgi-flask-docker uwsgi-flask/.
sudo docker compose up -d
