#!/bin/bash

clear
echo '... Processing images'
echo 'Insert hostname: '
read hostname
echo 'Username: '
read user
echo $user@$hostname

# remote_images='/home/mikcyons/www/wein/images'

rsync -aPu  $user@$hostname:/home/mikcyons/www/wein/images/* images

python3 main.py