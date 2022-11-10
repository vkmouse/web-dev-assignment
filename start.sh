cp week-6/py/config.json.template week-6/py/config.json
cp week-7/py/config.json.template week-7/py/config.json
sudo docker build -t web-uwsgi-flask-docker uwsgi-flask/.
sudo docker compose up -d
sudo docker restart web-week6-py
sudo docker restart web-week7-py
