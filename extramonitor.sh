#!/usr/bin/env bash
intern="eDP-1-1"
extern="HDMI-1-1"
choice=$1
if [[ -z $choice ]]; then
	choice=$(printf "disconnect\nconnect\nduplicate" | fzf)
fi

case "$choice" in
	"disconnect") xrandr --output "$intern" --off && xrandr --output "$extern" --mode 1920x1080;;
	"connect") xrandr --output "$intern" --auto --right-of "$extern";;
	"duplicate") xrandr --output "$extern" --auto --same-as "$intern" --mode 1920x1080 && xrandr --output "$intern" --mode 1920x1080;;
esac
~/.fehbg

