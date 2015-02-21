#!/usr/bin/env bash

# install most packages
apt-get update
apt-get install -y nginx python2.7 python-pip postgresql python-psycopg2 python-dev libldap2-dev libsasl2-dev libssl-dev python-pillow ruby ruby-compass redis-server

# install all python requirements
pip install -r /vagrant/requirements/dev.txt

# configure nginx
cp /vagrant/vagrant/nginx.conf /etc/nginx/sites-available/default
service nginx restart

# create postgres db
sudo -u postgres psql -c "CREATE USER vagrant" 2> /dev/null
sudo -u postgres psql -c "ALTER USER vagrant CREATEDB;"
sudo -u vagrant psql postgres -c "CREATE DATABASE caripi" 2> /dev/null

echo 'export DJANGO_SETTINGS_MODULE="realtime_demo.settings_vagrant"' | sudo -u vagrant tee -a ~vagrant/.bashrc
