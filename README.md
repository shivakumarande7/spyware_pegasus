# spyware_pegasus
# CyberFatRat — Ethical Spyware Simulator


![360](https://github.com/user-attachments/assets/60f10992-078d-4def-88c3-a9c8be47c516)

  
*A Python-based ethical spyware simulation tool for cybersecurity education and awareness.*

---

## 📌 **Disclaimer**
**CyberFatRat is strictly for educational and authorized penetration testing purposes.**  
- Do **not** use this tool for illegal or unauthorized activities.  
- The tool simulates spyware behaviors but does **not** perform actual harm or data theft.  
- Users are responsible for complying with local laws and obtaining proper permissions before testing.  

By using CyberFatRat, you agree to use it ethically and legally.

---

## 🚀 **Features**
| Module               | Simulation Purpose                          |
|----------------------|---------------------------------------------|
| **Webcam**           | Logs simulated webcam access.               |
| **Microphone**       | Simulates audio recording events.           |
| **Keylogger**        | Captures keystrokes in the terminal.        |
| **Clipboard**        | Monitors clipboard data (simulated).        |
| **GPS Spoofing**     | Generates mock coordinates and maps.        |
| **File Surveillance**| Tracks folder changes (create/edit/delete). |
| **C2 Interface**     | Simulates command-and-control operations.   |
| **Network Flood**    | Mimics SYN flood/DNS tunneling attacks.     |
| **Memory Theft**     | "Dumps" mock memory contents.               |
| **Suggester**        | Scans for vulnerabilities (Windows-only).   |
| **Report Generator** | Exports activity logs in HTML/PDF.          |

---

## 🛠 **Installation**
### Prerequisites
- Python 3.8+
- Pip (Python package manager)

### Steps
1. Clone the repository:
   bash
   git clone https://github.com/shivakumarande7/spyware_pegasus
   cd spyware_pegasus

   use this command after root
   bash
   python3 -m venv venv
   After click enter
   source bin/active/venv
   

3. Install dependencies:
   bash
   pip install -r requirements.txt
   
               or
   
   pip install pyfiglet termcolor keyboard pyperclip watchdog cryptography folium rich psutil

4. Run the tool:
   bash
   python main.py
   

---

## 🖥 **Usage**
### Starting the Tool
bash
python main.py

- The tool launches with an ASCII banner and a command menu.

### Commands
| Command               | Action                                      |
|-----------------------|---------------------------------------------|
| `/start mic`          | Simulate microphone recording.              |
| `/start webcam`       | Simulate webcam access.                     |
| `/start keylogger`    | Simulate keylogging (press `ESC` to stop).  |
| `/start memory`       | Simulate memory theft.                      |
| `/start gps`          | Spoof GPS coordinates.                      |
| `/suggester`          | Scan for vulnerabilities (Windows-only).    |
| `/report`             | Generate an activity report.                |
| `/exit`               | Exit the tool.                              |

---

## 📂 **Directory Structure**

CyberFatRat/
├── main.py                  # Entry point
├── modules/                 # Simulation modules
├── logs/                    # Activity logs
├── output/                  # Reports/encrypted data
├── utils/                   # Helpers (encryption, etc.)
├── templates/               # HTML/PDF templates
└── README.md                # This file


---

## 📜 **Legal Notice**
- **Authorized Use Only**: Ensure you have explicit permission to test the target system.  
- **No Warranty**: This tool is provided "as-is" without guarantees.  
- **Liability**: The developers are not responsible for misuse or damage caused by this tool.  

---

## 🔗 **Links**
- [YouTube Tutorials](https://youtube.com/@CyberFatRat)  
- [Report Issues](https://github.com/shivakumarande7/spyware_pegasus/issues)   

---

🛡 **Stay Ethical. Stay Legal. Happy Testing!**  


