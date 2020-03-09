#!/bin/bash
echo "Receiving, local signing and refreshing keys"
sudo pacman-key -r 74F5DE85A506BF64
sudo pacman-key --lsign-key 74F5DE85A506BF64
sudo pacman-key --refresh-keys
echo "###                 ArcoLinux key trusted                      ####"
