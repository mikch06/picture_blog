#!/bin/bash

# set -x

clear
echo '... Processing images'
echo 'Insert hostname: '
read hostname
echo 'Username: '
read user
echo $user@$hostname

remote_dir='/home/mikcyons/www/wein'

rsync -aPu  $user@$hostname:$remote_dir/images/* images

python3 main.py

rsync -aPu images/* $user@$hostname:$remote_dir/images/
rsync -aPu index.html $user@$hostname:$remote_dir
