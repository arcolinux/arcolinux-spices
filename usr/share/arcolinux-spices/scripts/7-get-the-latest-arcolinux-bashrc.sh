#!/bin/bash
echo "getting .bashrc from arcolinux-root"
mv $HOME/.bashrc $HOME/.bashrc-old
wget https://raw.githubusercontent.com/arcolinux/arcolinux-root/master/etc/skel/.bashrc-latest -O $HOME/.bashrc
source $HOME/.bashrc
echo "####    Your .bashrc has been overwritten with the ArcoLinux .bashrc      ####"
