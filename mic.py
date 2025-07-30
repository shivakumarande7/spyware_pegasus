import time
from datetime import datetime

def simulate_mic():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Microphone recording simulated at {current_time}")