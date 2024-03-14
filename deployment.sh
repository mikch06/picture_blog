#!/bin/bash

# set -x

clear
echo '... Processing images'
echo 'Insert hostname: '
read hostname
echo 'Username: '
read user
echo $user@$hostname

# Basedir on remote host
clear
echo "Sync from remote directory"
remote_dir='/home/mikcyons/www/wein'

# Sync down from remote host
rsync -aPu  $user@$hostname:$remote_dir/images/* images

python3 main.py

# Up sync all to remote host
echo "Sync to remote directory"
rsync -aPu images/* $user@$hostname:$remote_dir/images/
rsync -aPu index.html $user@$hostname:$remote_dir
