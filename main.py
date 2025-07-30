import os
import time
from termcolor import colored
from pyfiglet import Figlet
from modules import mic, webcam, gps, keylogger, clipboard, filesurveillance, c2, network_flood, suggester
from utils.report_generator import generate_report
from utils.encryption import encrypt_data

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
    print("/start c2 - Enter C2 command interface")
    print("/start flood - Simulate network flood")
    print("/suggester - Scan for vulnerabilities (Windows only)")
    print("/report - Generate activity report")
    print("/exit - Exit CyberFatRat")

    while True:
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
        elif command == "/start c2":
            c2.c2_interface()
        elif command == "/start flood":
            network_flood.simulate_flood()
        elif command == "/suggester":
            suggester.run_suggester()
        elif command == "/report":
            generate_report()
        elif command == "/exit":
            print("Exiting CyberFatRat...")
            break
        else:
            print("Invalid command. Type /help for available commands.")

if __name__ == "__main__":
    main()