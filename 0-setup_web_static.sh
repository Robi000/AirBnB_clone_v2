#!/usr/bin/env bash
# this will update the new server to the requirments
sudo apt -y update
sudo apt install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    ALX hbnb clone goes here...
  </body>
    </html>" | sudo tee -a /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i 's/\# pass PHP scripts to FastCGI server/location \/hbnb_static\/ {\
\n\t\talias \/data\/web_static\/current\/\;\n\t\tautoindex off\;\n\t}/' /etc/nginx/sites-available/default
sudo service nginx reload
