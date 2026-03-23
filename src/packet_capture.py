from scapy.all import sniff, IP, TCP
from ids_engine import detect_port_scan, detect_flood

packet_count = {}

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        
        # Count packets per IP
        packet_count[src_ip] = packet_count.get(src_ip, 0) + 1
        
        # Detect flooding
        if detect_flood(src_ip, packet_count[src_ip]):
            print(f"[ALERT] Flood attack detected from {src_ip}")
        
        # Detect port scanning
        if packet.haslayer(TCP):
            dst_port = packet[TCP].dport
            if detect_port_scan(src_ip, dst_port):
                print(f"[ALERT] Port scan detected from {src_ip}")

def start_capture():
    print("Starting packet capture...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_capture()
