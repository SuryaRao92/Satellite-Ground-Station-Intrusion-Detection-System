def detect_anomaly(packet_size, threshold=1000):
    """
    Simple anomaly detection based on packet size
    """
    if packet_size > threshold:
        return True
    return False
