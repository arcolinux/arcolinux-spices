#!/bin/bash
echo "Getting the latest arcolinux mirrors file"
sudo pacman -S wget --noconfirm --needed
sudo wget https://raw.githubusercontent.com/arcolinux/arcolinux-mirrorlist/master/etc/pacman.d/arcolinux-mirrorlist -O /etc/pacman.d/arcolinux-mirrorlist
echo '
#[arcolinux_repo_testing]
#SigLevel = Required DatabaseOptional
#Include = /etc/pacman.d/arcolinux-mirrorlist

[arcolinux_repo]
SigLevel = Required DatabaseOptional
Include = /etc/pacman.d/arcolinux-mirrorlist

[arcolinux_repo_3party]
SigLevel = Required DatabaseOptional
Include = /etc/pacman.d/arcolinux-mirrorlist

[arcolinux_repo_xlarge]
SigLevel = Required DatabaseOptional
Include = /etc/pacman.d/arcolinux-mirrorlist' | sudo tee --append /etc/pacman.conf
sudo pacman -Syy
echo "Installing the official mirrorlist file now."
echo "It will overwrite the one we downloaded earlier on."
sudo pacman -S arcolinux-mirrorlist-git --noconfirm
echo "####              ArcoLinux repo's have been added             ####"
