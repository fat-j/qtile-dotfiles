#!/bin/bash
redshift -O 2900 
brightnessctl 17500 
nm-applet &
fcitx5 &

setxkbmap -option caps:escape &

# Apply wallpaper using wal
wal -b 282738 -i ~/Wallpaper/Next-KDE-Material.png 

# Start picom
picom --config ~/.config/picom/picom.conf &
