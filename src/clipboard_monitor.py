import threading
import pyperclip
import time

class ClipboardMonitor:
    def __init__(self, manager):
        self.manager = manager
        self.running = False
        self.thread = threading.Thread(target=self.monitor_clipboard)

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def monitor_clipboard(self):
        previous_text = ""
        while self.running:
            try:
                text = pyperclip.paste()
                if text != previous_text:
                    previous_text = text
                    self.manager.copy_text(text)
            except pyperclip.PyperclipException:
                pass
            time.sleep(1)
