<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:1a0a00,100:2d1500&height=200&section=header&text=SyntecxHub%20%F0%9F%9B%A1%EF%B8%8F&fontSize=52&fontColor=ff8c00&animation=fadeIn&fontAlignY=38&desc=Cyber%20Security%20Internship%20Portfolio&descAlignY=60&descSize=20&descColor=ffb347" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=FF8C00&center=true&vCenter=true&width=700&lines=Port+Scanner+with+GUI+%26+PDF+Reports+%F0%9F%94%8D;Encrypted+Chat+App+%7C+End-to-End+Security+%F0%9F%94%90;Web+Vulnerability+Scanner+%7C+XSS+Detection+%F0%9F%95%B7%EF%B8%8F;CVE+Scanner+%7C+CVSS+Risk+Assessment+%F0%9F%93%8A;100%25+Python+%7C+Real+Tools+Built+From+Scratch+%F0%9F%90%8D;SyntecxHub+Virtual+Cyber+Security+Internship+%F0%9F%9A%80" alt="Typing SVG" />
</a>

<br/>

<!-- Badges Row -->
![SyntecxHub](https://img.shields.io/badge/SyntecxHub-Internship-ff8c00?style=for-the-badge&logo=shield&logoColor=white)
![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-✅%20Completed-00ff88?style=for-the-badge)
![Duration](https://img.shields.io/badge/Duration-Mar–Apr%202026-ff8c00?style=for-the-badge)
![Mode](https://img.shields.io/badge/Mode-Remote%20Virtual-ffb347?style=for-the-badge)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=CyberNiteshHub&color=ff8c00&style=flat-square&label=Profile+Views)
&nbsp;
[![GitHub followers](https://img.shields.io/github/followers/CyberNiteshHub?label=Follow&style=social)](https://github.com/CyberNiteshHub)

</div>

---

<div align="center">

## 🏢 About This Internship

</div>

> 🔨 **100% Practical & Project-Driven** — Unlike theory-based programs, this SyntecxHub internship involved **building real, working cybersecurity tools from scratch** using Python. Every week delivered a new tool — from network scanners to encrypted chat systems and CVE reporters.

<table>
<tr>
<td>🏆 <b>Organization</b></td><td>SyntecxHub</td>
<td>📅 <b>Duration</b></td><td>March 2026 – April 2026</td>
</tr>
<tr>
<td>👤 <b>Intern</b></td><td>Nitesh Verma (Cyber Nitesh)</td>
<td>🌍 <b>Mode</b></td><td>Remote (Virtual)</td>
</tr>
<tr>
<td>🐍 <b>Language</b></td><td>Python 3.x (100%)</td>
<td>🎯 <b>Approach</b></td><td>Hands-On Project-Based</td>
</tr>
<tr>
<td>📜 <b>Certification</b></td><td>✅ Certificate + Offer Letter</td>
<td>🎖️ <b>Badge ID</b></td><td>SH07CNGP7SEsbnK</td>
</tr>
</table>

---

<div align="center">

## 🗺️ 4-Week Internship Roadmap

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   WEEK 1              WEEK 2             WEEK 3              WEEK 4      ║
║                                                                          ║
║  🔍 Port Scanner ──► 🔐 Encrypted  ──► 🕷️ Web Vuln    ──► 📊 CVE        ║
║     + GUI               Chat App          Scanner              Scanner   ║
║     + PDF Report        + E2E Encryption  + XSS Detection      + CVSS   ║
║                                                                          ║
║  Socket + Tkinter    Socket + Crypto    BeautifulSoup       NVD API +   ║
║  ReportLab           Threading          Requests + GUI      ReportLab   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📚 Projects Overview

<details>
<summary><h3>1️⃣ &nbsp; Port Scanner Tool &nbsp; 🔍</h3></summary>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-ff8c00?style=flat-square)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-red?style=flat-square)
![Sockets](https://img.shields.io/badge/Network-Socket-4EAA25?style=flat-square&logo=linux)
![Status](https://img.shields.io/badge/Status-Completed-00ff88?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐%20Medium-yellow?style=flat-square)

**Objective:** Build a sophisticated GUI-based network scanner that identifies open ports, detects running services, and auto-generates professional PDF reports.

---

**✨ Key Features:**

| Feature | Description |
|---------|-------------|
| 🖥️ **GUI Interface** | User-friendly Tkinter desktop application |
| 🔍 **Port Scanning** | TCP port detection across configurable ranges |
| 📊 **Service Detection** | Identifies services running on open ports |
| 📄 **PDF Reports** | Auto-generated professional reports via ReportLab |
| ⚡ **Multi-Threading** | Fast concurrent scanning for performance |
| 💾 **Data Export** | Save scan results for future reference |

---

**🏗️ Architecture:**
```
┌─────────────────────────────────────────────────┐
│              PORT SCANNER FLOW                  │
│                                                 │
│   User Input (IP/Range)                         │
│         │                                       │
│         ▼                                       │
│   Tkinter GUI Layer ←──── Thread Manager        │
│         │                                       │
│         ▼                                       │
│   Socket.connect() × N ports (multi-thread)     │
│         │                                       │
│         ▼                                       │
│   Service Detection (socket.getservbyport)      │
│         │                                       │
│         ▼                                       │
│   Results Display + PDF Report Generation       │
└─────────────────────────────────────────────────┘
```

**Project Structure:**
```
Task1-Port_Scanner/
├── 🐍 scanner.py           ← Main application
├── 📋 requirements.txt     ← Dependencies
├── 📄 report.pdf           ← Sample output report
├── 📝 README.md            ← Documentation
└── 📸 screenshots/         ← 6 implementation images
    ├── source-code.png
    ├── run-file.png
    ├── scanning-result.png
    ├── save-report.png
    ├── save-pdf.png
    └── report-pdf.png
```

```bash
cd Task1-Port_Scanner
pip install -r requirements.txt
python scanner.py
```

📁 `Task1-Port_Scanner/` &nbsp;|&nbsp; 📸 **6 Screenshots** &nbsp;|&nbsp; 📄 [Sample Report](Task1-Port_Scanner/report.pdf) &nbsp;|&nbsp; ~200-300 Lines of Code

</details>

---

<details>
<summary><h3>2️⃣ &nbsp; Encrypted Chat Application &nbsp; 🔐</h3></summary>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Sockets](https://img.shields.io/badge/Network-TCP%20Sockets-4EAA25?style=flat-square)
![Cryptography](https://img.shields.io/badge/Encryption-AES%2FDES-ff8c00?style=flat-square)
![Threading](https://img.shields.io/badge/Concurrency-Threading-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-00ff88?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐%20Hard-orange?style=flat-square)

**Objective:** Build a real-time encrypted chat system with client-server architecture, supporting multiple simultaneous clients with end-to-end encrypted messaging.

---

**✨ Key Features:**

| Feature | Description |
|---------|-------------|
| 🔐 **E2E Encryption** | Messages encrypted before transmission |
| 💬 **Real-Time Messaging** | Socket-based instant communication |
| 👥 **Multi-Client** | Server handles multiple simultaneous clients |
| 🔑 **Key Management** | Secure key exchange mechanism |
| 🖥️ **CLI Interface** | Clean command-line chat experience |
| 📡 **TCP Reliability** | Reliable message delivery via TCP sockets |

---

**🏗️ Architecture:**
```
┌──────────────────────────────────────────────────────────────┐
│                    ENCRYPTED CHAT SYSTEM                      │
│                                                               │
│   CLIENT 1              SERVER               CLIENT 2         │
│      │                     │                    │             │
│   Encrypt ──► Send ──► Receive ──► Broadcast ──► Decrypt     │
│      │                     │                    │             │
│   Decrypt ◄── Recv ◄── Receive ◄── Broadcast ◄── Encrypt     │
│                                                               │
│   Algorithm: AES/DES  |  Key Exchange: Secure Share          │
│   Threading: Per-client handler thread on server              │
└──────────────────────────────────────────────────────────────┘
```

**Project Structure:**
```
Task2-Encrypted_chat_app/
├── 🐍 server.py            ← Server-side application
├── 🐍 client.py            ← Client-side application
├── 📋 requirements.txt     ← Dependencies (cryptography)
├── 📝 README.md            ← Documentation
└── 📸 screenshorts/        ← 9 implementation images
    ├── server_code.png
    ├── client_code.png
    ├── run-server.png
    ├── run-client1.png     ← Multi-client demo
    ├── run-client2.png
    ├── message-client1.png
    ├── message-client2.png
    ├── clients-conversation1.png
    └── clients-conversation2.png
```

```bash
# Terminal 1 — Start Server
python server.py

# Terminal 2 — Client 1
python client.py

# Terminal 3 — Client 2
python client.py
```

📁 `Task2-Encrypted_chat_app/` &nbsp;|&nbsp; 📸 **9 Screenshots** &nbsp;|&nbsp; ~300-400 Lines of Code

</details>

---

<details>
<summary><h3>3️⃣ &nbsp; Web Vulnerabilities Scanner &nbsp; 🕷️</h3></summary>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/Parsing-BeautifulSoup4-4EAA25?style=flat-square)
![Requests](https://img.shields.io/badge/HTTP-Requests-ff8c00?style=flat-square)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-00ff88?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐%20Hard-orange?style=flat-square)

**Objective:** Build an automated web security scanner that crawls web applications and detects XSS, SQL injection, and other vulnerabilities with a GUI interface.

---

**🚨 Vulnerability Types Detected:**

| Vulnerability | Type | Detection Method |
|---------------|------|-----------------|
| **XSS — Stored** | 🔴 High | Injected payload persists in response |
| **XSS — Reflected** | 🔴 High | Payload echoed back immediately |
| **XSS — DOM-based** | 🟠 High | DOM manipulation detection |
| **SQL Injection** | 🔴 Critical | Error-based pattern matching |
| **Input Validation** | 🟡 Medium | Unvalidated special chars |
| **Command Injection** | 🔴 Critical | Command vector testing |

---

**🔬 XSS Payloads Tested:**
```javascript
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<body onload=alert('XSS')>
" onmouseover="alert('XSS')
javascript:alert('XSS')
```

**🏗️ Scanning Process:**
```
URL Input
   │
   ▼
Page Crawling (BeautifulSoup)
   │
   ├──► Form Discovery
   ├──► Input Field Mapping
   └──► Link Extraction
           │
           ▼
   Payload Injection Testing (Requests)
           │
           ▼
   Response Analysis
           │
   ┌───────┴────────┐
   │                │
Vulnerable      Not Vulnerable
   │
   ▼
Report Generation (ReportLab PDF)
```

**Project Structure:**
```
Task3-Web_Vulnerabilities_Scanning/
├── 🐍 scanner.py           ← Main vulnerability scanner
├── 📋 requirements.txt     ← Dependencies
├── 📝 README.md            ← Documentation
└── 📸 screenshorts/        ← 5 implementation images
    ├── source_code.png
    ├── run_program.png
    ├── run_localserver.png
    ├── browse_localserver.png
    └── scanning_web_velnerability.png
```

```bash
cd Task3-Web_Vulnerabilities_Scanning
pip install -r requirements.txt
python scanner.py
```

📁 `Task3-Web_Vulnerabilities_Scanning/` &nbsp;|&nbsp; 📸 **5 Screenshots** &nbsp;|&nbsp; ~300-350 Lines of Code

</details>

---

<details>
<summary><h3>4️⃣ &nbsp; CVE Scanner & Vulnerability Reporter &nbsp; 📊</h3></summary>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NVD API](https://img.shields.io/badge/API-NVD%20%2F%20CVE%20Database-ff8c00?style=flat-square)
![CVSS](https://img.shields.io/badge/Scoring-CVSS%20v3.1-red?style=flat-square)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-purple?style=flat-square)
![ReportLab](https://img.shields.io/badge/PDF-ReportLab-4EAA25?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-00ff88?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-⭐⭐⭐⭐%20Advanced-red?style=flat-square)

**Objective:** Build an advanced CVE lookup and risk assessment tool that queries live vulnerability databases, calculates CVSS scores, and generates comprehensive professional PDF reports.

---

**✨ Feature Breakdown:**

| Feature | Details |
|---------|---------|
| 🔍 **CVE Lookup** | Search by software name, version, or CVE-ID |
| 📊 **CVSS v3.1** | Industry-standard vulnerability scoring |
| 🎯 **Risk Categorization** | Critical → High → Medium → Low → Info |
| 💥 **Impact Analysis** | Affected components, attack vectors |
| 🔧 **Mitigation Guidance** | Step-by-step remediation advice |
| 📄 **PDF Reports** | Full executive-level professional reports |
| 📈 **Historical Tracking** | Monitor vulnerabilities over time |
| 💾 **Multi-Format Export** | Multiple data export options |

---

**🏗️ Scanning Workflow:**
```
┌─────────────────────────────────────────────────────┐
│                CVE SCAN WORKFLOW                    │
│                                                     │
│  1. User Input (software / IP / domain)             │
│             │                                       │
│             ▼                                       │
│  2. Query NVD / CVE Database via API                │
│             │                                       │
│             ▼                                       │
│  3. Parse & Filter Results                          │
│             │                                       │
│     ┌───────┼───────┐                               │
│  🔴 Crit  🟠 High  🟡 Med  🟢 Low                  │
│             │                                       │
│             ▼                                       │
│  4. Calculate CVSS v3.1 Scores                      │
│             │                                       │
│             ▼                                       │
│  5. Generate PDF Report (Executive Summary          │
│     + Vulnerability List + Remediation Steps)       │
└─────────────────────────────────────────────────────┘
```

**Sample Scan Target:** `altoro.testfire.net`
```
CVE Scan Results:
├── 🔴 Critical Vulnerabilities: X
├── 🟠 High Vulnerabilities:     Y
├── 🟡 Medium Vulnerabilities:   Z
└── 📄 Report: Vulnerability_Report_[altoro.testfire.net].pdf
```

**Project Structure:**
```
Task4-CVE_Scanner/
├── 🐍 scanner.py                                    ← Main CVE scanner
├── 📋 requirements.txt                              ← Dependencies
├── 📝 README.md                                     ← Documentation
├── 📄 Vulnerability_Report_[altoro.testfire.net].pdf ← Real sample report
├── 📄 Cyber Security Task 4.pdf                    ← Task requirements
└── 📸 screenshots/                                  ← 6 implementation images
    ├── source_code.png
    ├── Project_GUI.png
    ├── run_project.png
    ├── CVE_Scan.png
    ├── generate_report_pdf.png
    └── final_pdf_report.png
```

```bash
cd Task4-CVE_Scanner
pip install -r requirements.txt
python scanner.py
```

📁 `Task4-CVE_Scanner/` &nbsp;|&nbsp; 📸 **6 Screenshots** &nbsp;|&nbsp; 📄 [Sample Vuln Report](Task4-CVE_Scanner/Vulnerability_Report_[altoro.testfire.net].pdf) &nbsp;|&nbsp; ~400-500 Lines of Code

</details>

---

## 🛠️ Tech Stack

<div align="center">

### 🐍 Core Language
![Python](https://img.shields.io/badge/Python_3.x-100%25-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 🖥️ GUI Development
![Tkinter](https://img.shields.io/badge/Tkinter-Desktop%20GUI-ff8c00?style=for-the-badge)

### 🌐 Networking & Communication
![Sockets](https://img.shields.io/badge/Socket_Programming-TCP%2FUDP-4EAA25?style=for-the-badge&logo=linux&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%20Client-ffb347?style=for-the-badge)
![Threading](https://img.shields.io/badge/Threading-Concurrency-purple?style=for-the-badge)

### 🔐 Security & Cryptography
![Cryptography](https://img.shields.io/badge/Cryptography-AES%2FDES-ff0000?style=for-the-badge)
![Hashlib](https://img.shields.io/badge/Hashlib-Hashing-ff8c00?style=for-the-badge)

### 🔍 Web & Parsing
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-HTML%20Parsing-4EAA25?style=for-the-badge)
![NVD API](https://img.shields.io/badge/NVD_API-CVE%20Database-red?style=for-the-badge)

### 📄 Reporting
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Generation-ffb347?style=for-the-badge)

### 🖥️ OS & Tools
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

## 📊 Skills Gained

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║                    SKILL PROGRESSION CHART                       ║
╠══════════════════════════╦═══════════════════════════════════════╣
║ Network Programming      ║ ████████████████████ 100%            ║
║ Socket Client-Server     ║ ████████████████████ 100%            ║
║ Cryptography & AES       ║ █████████████████░░░  85%            ║
║ GUI Dev (Tkinter)        ║ ████████████████████ 100%            ║
║ Web Scraping / Parsing   ║ ████████████████████ 100%            ║
║ XSS / Vuln Detection     ║ ██████████████████░░  90%            ║
║ CVE / CVSS Assessment    ║ ████████████████████ 100%            ║
║ PDF Report Generation    ║ ████████████████████ 100%            ║
║ Multi-Threading Python   ║ █████████████████░░░  85%            ║
║ Security Documentation   ║ ████████████████████ 100%            ║
╚══════════════════════════╩═══════════════════════════════════════╝
```

</div>

### 🌐 Network Programming
`TCP/IP Sockets` `Port Scanning` `Service Enumeration` `Client-Server Architecture` `Multi-Threading`

### 🔐 Cryptography & Security
`AES Encryption` `DES` `Key Management` `Secure Message Transmission` `Hash Functions`

### 🕷️ Web Security
`XSS Detection` `SQL Injection Patterns` `Payload Testing` `OWASP Top 10` `HTTP Analysis`

### 📊 Vulnerability Management
`CVE Research` `CVSS v3.1 Scoring` `Risk Assessment` `Remediation Planning` `NVD API Integration`

### 🖥️ GUI & Dev Practices
`Tkinter Framework` `Multi-Threaded GUIs` `Event Handling` `PDF Generation` `Git Version Control`

---

## 📂 Full Repository Structure

```
Syntecxhub-Cyber-Security-Internship/
│
├── 📂 Task1-Port_Scanner/                    🔍 Port Scanning Tool
│   ├── 🐍 scanner.py                         (Main GUI application)
│   ├── 📋 requirements.txt                   (Dependencies)
│   ├── 📄 report.pdf                         (Sample scan report)
│   ├── 📝 README.md                          (Documentation)
│   └── 📸 screenshots/                       (6 images)
│
├── 📂 Task2-Encrypted_chat_app/              🔐 Encrypted Chat System
│   ├── 🐍 server.py                          (Server application)
│   ├── 🐍 client.py                          (Client application)
│   ├── 📋 requirements.txt                   (Dependencies)
│   ├── 📝 README.md                          (Documentation)
│   └── 📸 screenshorts/                      (9 images)
│
├── 📂 Task3-Web_Vulnerabilities_Scanning/   🕷️ Web Vulnerability Scanner
│   ├── 🐍 scanner.py                         (Main scanner)
│   ├── 📋 requirements.txt                   (Dependencies)
│   ├── 📝 README.md                          (Documentation)
│   └── 📸 screenshorts/                      (5 images)
│
├── 📂 Task4-CVE_Scanner/                     📊 CVE Scanner & Reporter
│   ├── 🐍 scanner.py                         (Main CVE tool)
│   ├── 📋 requirements.txt                   (Dependencies)
│   ├── 📝 README.md                          (Documentation)
│   ├── 📄 Vulnerability_Report_[altoro].pdf  (Real sample report)
│   └── 📸 screenshots/                       (6 images)
│
├── 📂 Certificates/                          🎖️ Internship Documents
│   ├── 📄 Offer_Letter_Nitesh_.pdf
│   └── 🏅 SH07CNGP7SEsbnK.png
│
└── 📄 README.md
```

---

## ✅ Project Completion Summary

<div align="center">

| # | Project | Tools | Difficulty | Code | Report | Screenshots |
|---|---------|-------|-----------|------|--------|-------------|
| 1 | Port Scanner | Python, Tkinter, Socket, ReportLab | ⭐⭐ Medium | ~250 lines | [📄](Task1-Port_Scanner/report.pdf) | [📸 6](Task1-Port_Scanner/screenshots/) |
| 2 | Encrypted Chat | Python, Socket, Cryptography, Threading | ⭐⭐⭐ Hard | ~350 lines | — | [📸 9](Task2-Encrypted_chat_app/screenshorts/) |
| 3 | Web Vuln Scanner | Python, BS4, Requests, Tkinter | ⭐⭐⭐ Hard | ~325 lines | — | [📸 5](Task3-Web_Vulnerabilities_Scanning/screenshorts/) |
| 4 | CVE Scanner | Python, NVD API, CVSS, Tkinter, ReportLab | ⭐⭐⭐⭐ Advanced | ~450 lines | [📄](Task4-CVE_Scanner/Vulnerability_Report_[altoro.testfire.net].pdf) | [📸 6](Task4-CVE_Scanner/screenshots/) |

**Total: 4 Projects &nbsp;|&nbsp; 1000+ Lines of Code &nbsp;|&nbsp; 40+ Screenshots &nbsp;|&nbsp; 2 PDF Reports**

</div>

---

## 🔐 Security Best Practices Implemented

<div align="center">

| Principle | Implementation |
|-----------|---------------|
| 🛡️ **Defense in Depth** | Multiple security layers in each tool |
| 🔑 **Least Privilege** | Tools use only necessary permissions |
| ✅ **Data Validation** | Input sanitization across all projects |
| 🔒 **Secure Communication** | AES/DES encrypted data transmission |
| 🚫 **Error Handling** | Graceful failure without info leakage |
| 📋 **Audit Logging** | Activity tracking and reporting |
| 📢 **Responsible Disclosure** | Ethical testing and reporting practices |

</div>

---

## 📈 Week-by-Week Journey

<div align="center">

```
Week 1 ──► Week 2 ──► Week 3 ──► Week 4
  🔍           🔐           🕷️           📊
Port        Encrypted    Web Vuln     CVE
Scanner     Chat App     Scanner      Scanner
  │             │            │            │
Socket       Crypto       HTML         NVD
GUI          Server       Parsing      API
PDF          Client       XSS          CVSS
```

</div>

**Week 1 — Network Security:** Learned socket programming, built port scanner with Tkinter GUI and PDF report generation via ReportLab.

**Week 2 — Cryptography:** Studied AES/DES encryption algorithms, built client-server chat architecture with multi-client threading and end-to-end encrypted messaging.

**Week 3 — Web Security:** Analyzed XSS and injection vulnerabilities, implemented automated crawler and payload tester using BeautifulSoup and Requests.

**Week 4 — Vulnerability Management:** Integrated NVD/CVE database API, built CVSS v3.1 scoring system, and generated real professional PDF vulnerability reports.

---

## 🏆 Certifications & Achievements

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║              🏅 INTERNSHIP CERTIFICATE DETAILS                ║
╠═══════════════════════════════════════════════════════════════╣
║  Organization  :  SyntecxHub                                  ║
║  Program       :  Virtual Cyber Security Internship           ║
║  Duration      :  March 2026 – April 2026                     ║
║  Mode          :  Remote                                      ║
║  Status        :  ✅ Successfully Completed                   ║
║  Badge ID      :  SH07CNGP7SEsbnK                             ║
╚═══════════════════════════════════════════════════════════════╝
```

[![Certificate](https://img.shields.io/badge/📄%20Offer%20Letter-View%20PDF-ff8c00?style=for-the-badge)](Certificates/Offer_Letter_Nitesh_.pdf)
[![Badge](https://img.shields.io/badge/🏅%20Completion%20Badge-SH07CNGP7SEsbnK-ffb347?style=for-the-badge)](Certificates/SH07CNGP7SEsbnK.png)

</div>

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/CyberNiteshHub/Syntecxhub-Cyber-Security-Internship.git
cd Syntecxhub-Cyber-Security-Internship

# 2. Setup virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Run any project
cd Task1-Port_Scanner && pip install -r requirements.txt && python scanner.py
cd Task2-Encrypted_chat_app && pip install -r requirements.txt && python server.py
cd Task3-Web_Vulnerabilities_Scanning && pip install -r requirements.txt && python scanner.py
cd Task4-CVE_Scanner && pip install -r requirements.txt && python scanner.py
```

---

## 🔗 Resources & References

<div align="center">

[![OWASP Top 10](https://img.shields.io/badge/OWASP-Top%2010-000000?style=flat-square&logo=owasp)](https://owasp.org/www-project-top-ten/)
[![NVD NIST](https://img.shields.io/badge/NVD-NIST%20CVE%20DB-003087?style=flat-square)](https://nvd.nist.gov/)
[![CVE Details](https://img.shields.io/badge/CVE-Details%20DB-red?style=flat-square)](https://www.cvedetails.com/)
[![CVSS Calculator](https://img.shields.io/badge/CVSS-v3.1%20Calculator-ff8c00?style=flat-square)](https://www.first.org/cvss/calculator/3.1)
[![Python Docs](https://img.shields.io/badge/Python-Documentation-3776AB?style=flat-square&logo=python)](https://docs.python.org/3/)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Practice-red?style=flat-square)](https://tryhackme.com/)
[![HackTheBox](https://img.shields.io/badge/HackTheBox-Challenges-9fef00?style=flat-square)](https://www.hackthebox.com/)

</div>

---

## 🎯 What's Next?

Continuing to build advanced cybersecurity skills:

- 🔐 **Advanced Cryptography** — RSA, ECC, PKI systems
- 🤖 **ML for Threat Detection** — Anomaly detection models
- ☁️ **Cloud Security** — AWS/Azure security configurations
- 🔍 **Advanced Pentesting** — CTF competitions, bug bounty
- 📱 **Mobile Security** — Android/iOS app vulnerability assessment
- 🌐 **Advanced Web Security** — API security, OAuth flaws

---

## 📌 Quick Links

<div align="center">

[![Task 1](https://img.shields.io/badge/🔍%20Task%201-Port%20Scanner-ff8c00?style=for-the-badge)](Task1-Port_Scanner/README.md)
[![Task 2](https://img.shields.io/badge/🔐%20Task%202-Encrypted%20Chat-ff8c00?style=for-the-badge)](Task2-Encrypted_chat_app/README.md)
[![Task 3](https://img.shields.io/badge/🕷️%20Task%203-Web%20Scanner-ff8c00?style=for-the-badge)](Task3-Web_Vulnerabilities_Scanning/README.md)
[![Task 4](https://img.shields.io/badge/📊%20Task%204-CVE%20Scanner-ff8c00?style=for-the-badge)](Task4-CVE_Scanner/README.md)
[![Certificate](https://img.shields.io/badge/🏅%20Certificate-View-ffb347?style=for-the-badge)](Certificates/Offer_Letter_Nitesh_.pdf)

</div>

---

## 👨‍💻 Author

<div align="center">

<img src="https://github.com/CyberNiteshHub.png" width="100" style="border-radius:50%"/>

### Nitesh Verma — *Cyber Nitesh*
**Cyber Security Enthusiast | Python Developer | Ethical Hacker**

[![GitHub](https://img.shields.io/badge/GitHub-CyberNiteshHub-181717?style=for-the-badge&logo=github)](https://github.com/CyberNiteshHub)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nitesh%20Verma-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/nitesh-verma-4ba443363)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20Site-ff8c00?style=for-the-badge&logo=netlify)](https://cyberniteshportfolio.netlify.app)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail)](mailto:niteshkumar3133845@gmail.com)

</div>

---

## 🙏 Acknowledgments

- 🏆 **SyntecxHub Team** — For an exceptional project-driven learning environment
- 👩‍🏫 **Mentors** — For guidance, code reviews, and valuable feedback
- 🌍 **Open Source Community** — For tools and libraries powering these projects
- 🐉 **Kali Linux Community** — For the powerful security platform

---

<div align="center">

## ⚠️ Ethical Use & Disclaimer

> 🛡️ All tools were built and tested on **systems I own** or in **controlled lab environments**.
>
> These projects are strictly for **educational learning**, **skill building**, and **authorized testing**.
>
> **Unauthorized access to systems is illegal.** Always obtain explicit permission before testing any network or system.

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2d1500,50:1a0a00,100:0d0d0d&height=120&section=footer&text=Building%20Secure%20Systems%2C%20One%20Tool%20at%20a%20Time%20%F0%9F%9B%A1%EF%B8%8F&fontSize=16&fontColor=ff8c00&animation=fadeIn" width="100%"/>

**⭐ Star this repo if it helped you! | 🍴 Fork as your own template**

![Made with](https://img.shields.io/badge/Made%20with-❤️%20%26%20Python-ff8c00?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-May%202026-ffb347?style=flat-square)
![Lines of Code](https://img.shields.io/badge/Total%20Code-1000%2B%20Lines-3776AB?style=flat-square&logo=python)

</div>
