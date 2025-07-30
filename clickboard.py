import pyperclip
from datetime import datetime

def simulate_clipboard():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clipboard_data = pyperclip.paste()
    print(f"Clipboard data at {current_time}: {clipboard_data}")