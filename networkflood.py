import random
import time
from datetime import datetime

def simulate_flood():
    print("Simulating network flood...")
    for i in range(10):
        print(f"SYN flood packet sent to target at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(0.5)