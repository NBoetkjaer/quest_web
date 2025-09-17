#!/bin/sh

sudo cp quest-web-srv.service /etc/systemd/system/
sudo chmod u+rw /etc/systemd/system/quest-web-srv.service

sudo systemctl enable quest-web-srv

# Start the service
#sudo systemctl start quest-web-srv

# Stop the service
#sudo systemctl stop quest-web-srv