#!/bin/bash
echo "Receiving, local signing and refreshing keys"
#erik
pacman-key -r 74F5DE85A506BF64
pacman-key --lsign-key 74F5DE85A506BF64
#marco
pacman-key -r 74F5DE85A506BF64
pacman-key --lsign-key F1ABB772CE9F7FC0
#john
pacman-key -r 74F5DE85A506BF64
pacman-key --lsign-key 4B1B49F7186D8731
sudo pacman-key --refresh-keys
echo "###                 ArcoLinux key trusted                      ####"
