#!/bin/bash
echo "Installing polkit and polkit-gnome"
sudo pacman -S --noconfirm --needed polkit
sudo pacman -S --noconfirm --needed polkit-gnome
echo "####            Polkit and polkit-gnome are installed               ####"
