import datetime

def log_alert(message):
    timestamp = datetime.datetime.now()
    log = f"[{timestamp}] {message}"
    
    print(log)
    
    with open("data/sample_logs.txt", "a") as f:
        f.write(log + "\n")
