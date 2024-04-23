#!/bin/bash

# set -x

clear
# read hostname
# read user

if [ -z $1]
then
    echo ' >>> Exit'
    echo ''
    echo '     ---> Use user and hostname as $1 and $2'
    echo ''
    echo ''
    exit
    
fi

echo '... Processing images'

echo $user@$hostname

# Basedir on remote host
clear
remote_dir='/home/mikcyons/www/wein'

# Sync down from remote host
echo "Sync from remote directory"
rsync -aPu  $1@$2:$remote_dir/images/* images

# Convert image size
echo "Convert images to right size"
for i in images/*
do 
  convert -verbose $i -resize 1200x $i
done

# Run blog creator
python3 main.py

# Up sync all to remote host
echo ''
echo ''
echo "Sync to remote directory"
rsync -aPu images/* $1@$2:$remote_dir/images/
rsync -aPu index.html $1@$2:$remote_dir
echo 'All jobs done'
