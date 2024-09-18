import tkinter as tk
from src.clipboard_manager import ClipboardManager
from src.clipboard_monitor import ClipboardMonitor
import pyperclip
import tkinter.font as tkfont

class ClipboardApp:
    def __init__(self, root):
        self.manager = ClipboardManager()
        self.root = root
        self.root.title("Copy That")  
        self.root.geometry("400x300") 
        self.root.config(bg="#f5f5f5")  

        self.font = tkfont.Font(family="Helvetica", size=12)


        self.text_entry = tk.Entry(root, font=self.font, width=50, bg="#ffffff", bd=2, relief="solid")
        self.text_entry.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy", command=self.copy_text, font=self.font, bg="#4CAF50", fg="#ffffff", bd=0, padx=10, pady=5)
        self.copy_button.pack(pady=5)

        self.paste_button = tk.Button(root, text="Paste", command=self.paste_text, font=self.font, bg="#2196F3", fg="#ffffff", bd=0, padx=10, pady=5)
        self.paste_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear History", command=self.clear_history, font=self.font, bg="#f44336", fg="#ffffff", bd=0, padx=10, pady=5)
        self.clear_button.pack(pady=5)

        self.history_label = tk.Label(root, text="Clipboard History:", font=self.font, bg="#f5f5f5")
        self.history_label.pack(pady=10)

        self.history_listbox = tk.Listbox(root, font=self.font, width=50, height=10, bg="#ffffff", bd=2, relief="solid")
        self.history_listbox.pack(pady=10)
        self.history_listbox.bind('<Double-1>', self.paste_selected_text)

        self.update_history()

        self.monitor = ClipboardMonitor(self.manager)
        self.monitor.start()

    def copy_text(self):
        text = self.text_entry.get()
        self.manager.copy_text(text)
        self.update_history()

    def paste_text(self):
        if self.manager.get_history():
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, self.manager.get_history()[-1])
            pyperclip.copy(self.manager.get_history()[-1])  

    def paste_selected_text(self, event):
        selected_index = self.history_listbox.curselection()
        if selected_index:
            text = self.history_listbox.get(selected_index)
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, text)
            pyperclip.copy(text) 

    def clear_history(self):
        self.manager.clear_history()
        self.update_history()

    def update_history(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.manager.get_history():
            self.history_listbox.insert(tk.END, item)

    def on_closing(self):
        self.monitor.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
