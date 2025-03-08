# 🕶️ PACKET REAPER - A Python Packet Sniffer

## 🚀 Overview
**Packet Reaper** is a **powerful yet minimalistic** Python-based network packet sniffer built using **Scapy**. It captures and displays real-time network packets, revealing **IP, TCP, and UDP details** in a stylish, hacker-themed interface. 

---

## 🔹 Features
✅ **Real-time packet sniffing**  
✅ **Captures IP, TCP, and UDP packets**  
✅ **Displays source & destination addresses**   
✅ **Lightweight & efficient**  

---

## ⚙️ Installation
First, install the required dependencies:

```bash
pip install scapy
```

---

## 🎯 Usage
Run the script with administrative privileges:

```bash
sudo python packet_reaper.py  # Linux/Mac
```

On Windows (run as administrator):

```bash
python packet_reaper.py
```

Press `Ctrl+C` to stop sniffing.

---

## 📜 How It Works
1. Captures network packets in real time
2. Extracts **IP addresses, ports, and protocols**
3. Displays them in a structured format

Example output:

```
[🔥 2025-03-07 12:34:56 🔥] Packet Captured
📡 SRC: 192.168.1.5  ➝  DST: 8.8.8.8
🔗 TCP Port: 54321  ➝  443
```

---

## 🔧 Customization & Improvements
Want to enhance it? Try these:
✅ **Save packets to a log file**  
✅ **Filter by protocol (TCP, UDP, HTTP, DNS, etc.)**  
✅ **Capture raw packet data**  
✅ **Integrate with `tshark` for advanced analysis**  

---

## ⚠️ Disclaimer
This tool is for **educational and ethical** purposes **only**. Unauthorized use for malicious activities is **strictly prohibited**.

---

## 🛠️ Contributing
Feel free to fork this project, enhance it, and submit pull requests!

---

## 📜 License
MIT License - Free to modify and distribute.

---

🔗 **Happy Sniffing! Stay Ethical.** 🕶️
