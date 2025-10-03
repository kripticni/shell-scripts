#!/usr/bin/env bash
xrandr --output HDMI-0 --off
modeline=$(cvt 1920 1080 60 | grep Modeline)
modeline=${modeline:9} # trimming Modeline 
xrandr --newmode $modeline
xrandr --addmode HDMI-0 "1920x1080"
xrandr --output HDMI-0 --mode "1920x1080"
