#!/bin/bash

######################################################################################################################

sudo pacman -S wget --noconfirm --needed

echo "Getting the ArcoLinux keys from the ArcoLinux repo"

sudo wget https://github.com/arcolinux/arcolinux_repo/raw/master/x86_64/arcolinux-keyring-20230919-6-any.pkg.tar.zst -O /tmp/arcolinux-keyring-20230919-6-any.pkg.tar.zst
sudo pacman -U --noconfirm --needed /tmp/arcolinux-keyring-20230919-6-any.pkg.tar.zst

######################################################################################################################

echo "Getting the latest arcolinux mirrors file"

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

######################################################################################################################

# sudo pacman -S --noconfirm --needed expac
# sudo pacman -S --noconfirm --needed hwinfo
# sudo pacman -S --noconfirm --needed reflector
# sudo pacman -S --noconfirm --needed youtube-dl
# sudo pacman -S --noconfirm --needed yay-bin
# sudo pacman -S --noconfirm --needed neofetch

######################################################################################################################

echo "Getting .bashrc from arcolinux-root"
for i in `ls /home/`
do
	person=$i
done
wget https://raw.githubusercontent.com/arcolinux/arcolinux-root/master/etc/skel/.bashrc-latest -O /home/$person/bashrc-of-arcolinux
echo "####    The ArcoLinux bashrc has been downloaded and is in your home directory     ####"