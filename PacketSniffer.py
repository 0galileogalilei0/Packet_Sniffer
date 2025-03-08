from scapy.all import sniff
from datetime import datetime

ascii_banner = """
  ██████  █████  ██████  ███████  ██████  ███████ ██████  
 ██      ██   ██ ██   ██ ██      ██       ██      ██   ██ 
 ██      ███████ ██████  █████   ██   ███ █████   ██████  
 ██      ██   ██ ██   ██ ██      ██    ██ ██      ██   ██ 
  ██████ ██   ██ ██   ██ ███████  ██████  ███████ ██   ██ 

             ~ PACKET REAPER ~
         A Python Packet Sniffer  
"""

print(ascii_banner)


def process_packet(packet):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n[🔥 {timestamp} 🔥] Packet Captured")
    print(packet.summary())  # Print a high-level summary of the packet
    if packet.haslayer("IP"):
        print(f"📡 SRC: {packet['IP'].src}  ➝  DST: {packet['IP'].dst}")
    if packet.haslayer("TCP"):
        print(f"🔗 TCP Port: {packet['TCP'].sport}  ➝  {packet['TCP'].dport}")
    if packet.haslayer("UDP"):
        print(f"📡 UDP Port: {packet['UDP'].sport}  ➝  {packet['UDP'].dport}")


print("\n[🚀] Sniffing packets... Press Ctrl+C to stop.\n")
sniff(prn=process_packet, store=False)
