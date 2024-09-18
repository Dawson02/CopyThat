from src.clipboard_manager import ClipboardManager

def main():
    manager = ClipboardManager()

    # Example
    manager.copy_text("Hello, World!")
    print("Clipboard contents:", manager.get_clipboard_contents())
    print("Clipboard history:", manager.get_history())

if __name__ == "__main__":
    main()
