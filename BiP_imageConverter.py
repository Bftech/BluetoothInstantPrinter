# convert 01.jpg -rotate 90 -resize 384 -dither FloydSteinberg -remap pattern:gray50 01F.png

import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
#INIT

class ConversionObserver(PatternMatchingEventHandler):
    patterns = ["*.png", "*.jpg"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug

    def on_created(self, event):
        self.process(event)


#RUN
if __name__ == '__main__':
    convObserver = Observer()
    convObserver.schedule(ConversionObserver(), path="/home/pi/bluetoothUpload")
    convObserver.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        convObserver.stop()

    convObserver.join()
