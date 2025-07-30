from datetime import datetime
import os

def generate_report():
    report = f"""
    CyberFatRat Activity Report
    Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    ---
    Summary of Simulated Activities:
    - Webcam accessed
    - Microphone recorded
    - Keylogger active
    - Clipboard monitored
    - GPS spoofed
    - Files monitored
    - Network flood simulated
    ---
    Disclaimer: This tool is for educational purposes only.
    """
    with open("output/report.txt", "w") as f:
        f.write(report)
    print("Report generated at output/report.txt")