#!/bin/bash
echo "Installing the software ArcoLinux uses in .bashrc"
sudo pacman -S --noconfirm --needed expac
sudo pacman -S --noconfirm --needed hwinfo
sudo pacman -S --noconfirm --needed reflector
sudo pacman -S --noconfirm --needed youtube-dl
echo "###            Software for .bashrc is installed                ####"
