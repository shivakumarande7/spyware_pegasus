import os
import time
from datetime import datetime
from termcolor import colored
from pyfiglet import Figlet
from modules import (
    mic, 
    webcam, 
    gps, 
    keylogger, 
    clipboard, 
    filesurveillance, 
    c2, 
    network_flood, 
    suggester,
    memory_theft  # Added the new module
)

def display_banner():
    f = Figlet(font='slant')
    banner = f.renderText('CyberFatRat')
    print(colored(banner, 'cyan'))
    print(colored("Welcome to CyberFatRat — Your Ethical Spyware Simulator", 'yellow'))
    print(colored("Please do subscribe: youtube.com/@CyberFatRat", 'yellow'))

def main():
    display_banner()
    print("\nAvailable Commands:")
    print("/start mic - Simulate microphone recording")
    print("/start webcam - Simulate webcam access")
    print("/start keylogger - Simulate keylogger")
    print("/start clipboard - Simulate clipboard monitoring")
    print("/start gps - Simulate GPS spoofing")
    print("/start filesurveillance - Monitor folder for changes")
    print("/start memory - Simulate memory theft")  # Added new command
    print("/start c2 - Enter C2 command interface")
    print("/start flood - Simulate network flood")
    print("/suggester - Scan for vulnerabilities (Windows only)")
    print("/report - Generate activity report")
    print("/exit - Exit CyberFatRat")

    while True:
        try:
            command = input("\nCyberFatRat> ").strip().lower()
            
            if command == "/start mic":
                mic.simulate_mic()
            elif command == "/start webcam":
                webcam.simulate_webcam()
            elif command == "/start keylogger":
                keylogger.simulate_keylogger()
            elif command == "/start clipboard":
                clipboard.simulate_clipboard()
            elif command == "/start gps":
                gps.simulate_gps()
            elif command == "/start filesurveillance":
                filesurveillance.simulate_file_surveillance()
            elif command == "/start memory":  # Added new command handler
                memory_theft.memory_theft_interface()
            elif command == "/start c2":
                c2.c2_interface()
            elif command == "/start flood":
                network_flood.simulate_flood()
            elif command == "/suggester":
                suggester.run_suggester()
            elif command == "/report":
                from utils.report_generator import generate_report
                generate_report()
            elif command == "/exit":
                print("Exiting CyberFatRat...")
                break
            elif command == "/help":
                main()  # Show menu again
            else:
                print("Invalid command. Type /help for available commands.")
                
        except KeyboardInterrupt:
            print("\nUse /exit to quit properly")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()