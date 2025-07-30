import os
import random
import time
from datetime import datetime
from utils.encryption import encrypt_data

def simulate_memory_theft():
    """
    Simulates memory theft by "dumping" mock memory contents and logging the activity.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[+] Simulating memory theft at {current_time}")

    # Mock memory regions (for simulation)
    mock_memory_regions = [
        "0x00007FFA1A2B3C4D: [Credentials] admin:password123",
        "0x00007FFB2B3C4D5E: [Encryption Key] AES-256: 0x1F2E3D4C5B6A7988",
        "0x00007FFC3C4D5E6F: [Session Token] JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "0x00007FFD4D5E6F7A: [Private Key] RSA: -----BEGIN PRIVATE KEY-----...",
    ]

    # Simulate memory dumping
    print("[+] Dumping memory regions...")
    for region in mock_memory_regions:
        time.sleep(0.5)
        print(f"  -> Extracted: {region}")

    # Save "stolen" data to a log file (simulated)
    log_file = "logs/memory_theft.log"
    with open(log_file, "a") as f:
        f.write(f"Memory Theft Simulation at {current_time}\n")
        f.write("----------------------------------------\n")
        for region in mock_memory_regions:
            f.write(f"{region}\n")
        f.write("\n")

    # Encrypt the log file (simulated)
    print("[+] Encrypting exfiltrated data...")
    with open(log_file, "r") as f:
        data = f.read()
    encrypted_data, key = encrypt_data(data)
    with open("output/memory_theft_encrypted.bin", "wb") as f:
        f.write(encrypted_data)

    print(f"[+] Memory theft simulation complete. Encrypted data saved to output/memory_theft_encrypted.bin")
    print(f"[+] Decryption key (for simulation): {key.decode()}")

def memory_theft_interface():
    """
    Command interface for memory theft simulation.
    """
    print("\nMemory Theft Simulation Module")
    print("Commands:")
    print("  /start memory - Simulate memory theft")
    print("  /exit - Return to main menu")
    while True:
        cmd = input("MemoryTheft> ").strip().lower()
        if cmd == "/start memory":
            simulate_memory_theft()
        elif cmd == "/exit":
            break
        else:
            print("Invalid command. Type /exit to return.")