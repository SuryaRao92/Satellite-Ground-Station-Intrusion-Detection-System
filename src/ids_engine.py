from collections import defaultdict
import time

# Track ports accessed per IP
port_scan_tracker = defaultdict(list)

# Track packet timestamps
flood_tracker = defaultdict(list)

PORT_SCAN_THRESHOLD = 20
FLOOD_THRESHOLD = 50   # packets
TIME_WINDOW = 5        # seconds


def detect_port_scan(ip, port):
    current_time = time.time()
    port_scan_tracker[ip].append((port, current_time))
    
    # Remove old entries
    port_scan_tracker[ip] = [
        (p, t) for p, t in port_scan_tracker[ip]
        if current_time - t < TIME_WINDOW
    ]
    
    unique_ports = len(set(p for p, _ in port_scan_tracker[ip]))
    
    return unique_ports > PORT_SCAN_THRESHOLD


def detect_flood(ip, packet_count):
    current_time = time.time()
    flood_tracker[ip].append(current_time)
    
    flood_tracker[ip] = [
        t for t in flood_tracker[ip]
        if current_time - t < TIME_WINDOW
    ]
    
    return len(flood_tracker[ip]) > FLOOD_THRESHOLD
