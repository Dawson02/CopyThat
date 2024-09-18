import pyperclip

# Copy text to clipboard
pyperclip.copy('Hello, World!')

# Get text from clipboard
text = pyperclip.paste()
print(f'Clipboard text: {text}')