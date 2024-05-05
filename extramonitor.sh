#!/bin/bash
intern="eDP-1"
extern="HDMI-1"
case "$1" in
	"disconnect") xrandr --output "$intern" --off && xrandr --output "$extern" --mode 1920x1080;;
	"connect") xrandr --output "$intern" --auto --right-of "$extern";;
	"duplicate") xrandr --output "$extern" --auto --same-as "$intern" --mode 1920x1080 && xrandr --output "$intern" --mode 1920x1080;;
	*) echo "its disconnect/connect/duplicate" ;;
esac
~/.fehbg

