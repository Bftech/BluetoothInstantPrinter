# convert 01.jpg -rotate 90 -resize 384 -dither FloydSteinberg -remap pattern:gray50 01F.png
import time
import subprocess
import pyinotify
#INIT

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_CLOSE_WRITE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print "Uploaded:", event.pathname


handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

wdd = wm.add_watch('/home/pi/bluetoothUpload', mask, rec=True)
notifier.loop()
