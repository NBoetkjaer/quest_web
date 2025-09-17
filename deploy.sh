#!/bin/sh

hostname=webquest.local

RELATIVEDIR="quest_web/"
BASEDIR="\$HOME/$RELATIVEDIR"

echo " **** Stopping the service ****"
ssh $hostname "sudo systemctl stop quest-web-srv"
# Make directory and transfer source files.
ssh $hostname "mkdir -p $BASEDIR"
echo " **** Removing existing files ****"
ssh $hostname "cd $BASEDIR; sudo rm -r ./*"
# Copy new files.
echo " **** Starting to copy files ****"
scp ./*.*  $hostname:${RELATIVEDIR}
echo " **** Starting to copy boot files ****"
scp -r ./boot/* $hostname:${RELATIVEDIR}boot/
echo " **** Starting to copy static files ****"
scp -r ./static/*  $hostname:${RELATIVEDIR}static/
echo " **** Starting to copy templates files ****"
scp -r ./templates/* $hostname:${RELATIVEDIR}templates/

echo " **** Restarting the service ****"
ssh $hostname "sudo systemctl start quest-web-srv"


