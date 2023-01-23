#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo \
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ -f /data/web_static/current
chown -R ubuntu:ubuntu /data/

sed -z 's/\tserver_name _;/\tserver_name _;\n\tlocation \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\tindex index.html index.htm;\n\t\}/' -i /etc/nginx/sites-available/default

service nginx restart
