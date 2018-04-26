import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

#http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html
class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.txt", "*.csv"]

    def process(self, event):
        """"
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print event.src_path, event.event_type  # print now only for degug

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)
