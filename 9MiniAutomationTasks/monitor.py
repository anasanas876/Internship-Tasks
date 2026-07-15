# Task 3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging
import os

logging.basicConfig(
    filename="file.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        # Ignore folders
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            print(f"File Created: {file_name}")
            logging.info(f"New file created: {file_name}")


def file_monitoring():

    
    path = r"C:\Users\Ukasaa\Desktop\TestFolder"   
    
    handler = Handler()

    observer = Observer()

    observer.schedule(handler, path, recursive=False)

    observer.start()
    print("Monitoring started... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    file_monitoring()