def c2_interface():
    print("C2 Command Interface")
    print("Available commands: /start mic, /get logs, /encrypt exfil")
    while True:
        cmd = input("C2> ").strip().lower()
        if cmd == "/start mic":
            print("Microphone simulation started.")
        elif cmd == "/get logs":
            print("Fetching logs...")
        elif cmd == "/encrypt exfil":
            print("Encrypting and exfiltrating data...")
        elif cmd == "/exit":
            break
        else:
            print("Invalid command.")