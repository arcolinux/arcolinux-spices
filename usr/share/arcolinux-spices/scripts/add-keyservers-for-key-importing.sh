#!/bin/bash
#[ -d $HOME"/.gnupg" ] || mkdir -p $HOME"/.gnupg"
# echo "Adding keyservers to your personal .gpg for future applications"
# echo "that require keys to be imported with yay for example"
# echo '
# keyserver hkp://pool.sks-keyservers.net:80
# keyserver hkps://hkps.pool.sks-keyservers.net:443
# keyserver hkp://ipv4.pool.sks-keyservers.net:11371' | tee --append ~/.gnupg/gpg.conf
# chmod 600 ~/.gnupg/gpg.conf
# chmod 700 ~/.gnupg
echo "Adding keyservers to the /etc/pacman.d/gnupg folder for the use with pacman"
echo '
keyserver hkp://pool.sks-keyservers.net:80
keyserver hkps://hkps.pool.sks-keyservers.net:443
keyserver hkp://ipv4.pool.sks-keyservers.net:11371' | sudo tee --append /etc/pacman.d/gnupg/gpg.conf
echo "####          Keyservers with ports have been added to /etc/pacman.d/gnupg/gpg.conf            ####"
