from src.ids_engine import detect_port_scan

def test_port_scan():
    ip = "192.168.1.1"
    
    result = False
    
    for port in range(25):
        result = detect_port_scan(ip, port)
    
    assert result == True
