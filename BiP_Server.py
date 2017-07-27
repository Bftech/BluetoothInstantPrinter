# convert 01.jpg -rotate 90 -resize 384 -dither FloydSteinberg -remap pattern:gray50 01F.png
import time
import os
import subprocess
import pyinotify
from PIL import Image
from Adafruit_Thermal import *

#INIT
printer = Adafruit_Thermal("/dev/serial0", 9600, timeout=5)

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_CLOSE_WRITE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        if event.pathname.endswith("_FloydSteinberg-converted.png"):
            #print
            print "Printing:", event.pathname
            printer.printImage(Image.open(event.pathname), True)

        if not event.pathname.endswith("_FloydSteinberg-converted.png") and event.pathname.endswith(".png") or event.pathname.endswith(".jpg") or event.pathname.endswith(".PNG") or event.pathname.endswith(".JPG"):
            #convert
            print "Uploaded:", event.pathname
            print "Converting..."
            subprocess.call(['convert', event.pathname, '-rotate', '90', '-resize', '384', '-dither', 'FloydSteinberg', '-remap', 'pattern:gray50', event.pathname + "_FloydSteinberg-converted.png"])
            print "Converted !"

        if event.name == "shutdown.txt":
            print "shutdown"
            subprocess.call(["sudo", "shutdown", "now"])



#RUN
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

wdd = wm.add_watch('/home/pi/bluetoothUpload', mask)
notifier.loop()
