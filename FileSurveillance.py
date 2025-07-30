import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"File modified: {event.src_path} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def on_created(self, event):
        print(f"File created: {event.src_path} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def simulate_file_surveillance():
    path = input("Enter folder path to monitor: ")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Monitoring folder: {path}. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()