import pyperclip

class ClipboardManager:
    def __init__(self):
        self.clipboard_history = []

    def copy_text(self, text):
        pyperclip.copy(text)
        if text not in self.clipboard_history:
            self.clipboard_history.append(text)

    def get_clipboard_contents(self):
        return pyperclip.paste()
    
    def get_history(self):
        return self.clipboard_history

    def clear_history(self):
        self.clipboard_history = []