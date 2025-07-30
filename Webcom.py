import time
from datetime import datetime

def simulate_webcam():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Webcam accessed at {current_time}")