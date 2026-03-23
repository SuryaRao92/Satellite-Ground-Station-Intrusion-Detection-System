# Satellite-Ground-Station-Intrusion-Detection-System
# 🛰️ Satellite Ground Station Intrusion Detection System (IDS)

## 📌 Overview

This project implements a real-time Intrusion Detection System (IDS) for satellite ground station communication networks.

It monitors network traffic and detects potential cyber threats such as:

* Port scanning attacks
* Flooding (DoS) attacks
* Abnormal traffic patterns

## 🚀 Features

* Real-time packet capture using Scapy
* Detection of reconnaissance attacks (port scanning)
* Flooding attack detection based on traffic spikes
* Lightweight Flask-based monitoring dashboard

## 🛠️ Tech Stack

* Python
* Scapy
* Flask

## 📊 Architecture

1. Packet Capture Layer
2. Detection Engine
3. Alert System
4. Visualization Dashboard

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/packet_capture.py
python web/app.py
```

## 📈 Future Improvements

* Machine Learning-based anomaly detection
* Integration with SIEM tools
* Satellite protocol simulation (CCSDS)

## 👨‍💻 Author

[Your Name]
