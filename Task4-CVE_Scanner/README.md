# Advanced CVE Vulnerability Scanner (GUI)

## 📌 Project Overview
The **Advanced CVE Vulnerability Scanner** is a robust, Python-based graphical network utility designed for Debian/Kali Linux systems. It actively scans target IP addresses or domains, detects open ports and active services, performs banner grabbing to extract software versions, and correlates this data against a local CVE (Common Vulnerabilities and Exposures) dictionary.

This tool aims to automate the initial reconnaissance phase of penetration testing and outputs professional, structured PDF reports.

## ✨ Features
- **Port Scanning:** Rapidly scans common TCP ports using standard socket protocols.
- **Service Detection & Banner Grabbing:** Extracts service versions (e.g., Apache, OpenSSH).
- **Vulnerability Mapping:** Cross-references grabbed banners with a local CVE database to highlight known exploits.
- **Multi-threading Engine:** Keeps the GUI responsive and ensures fast network operations.
- **Dynamic Terminal GUI:** Dark cyber-themed interface built natively with Tkinter, featuring real-time colored log outputs.
- **PDF Report Generation:** Compiles findings into a clean, professional PDF file using `reportlab`.

## ⚙️ Requirements & Installation
This project was built and tested on Kali Linux. 

1. Ensure Python 3.x is installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
