#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    If you can read this, it worked!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

if ! grep -q '^\s*location /hbnb_static/ {' /etc/nginx/sites-available/default; then
    sudo sed -i '/^\s*location \/ {$/i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi

sudo service nginx restart
