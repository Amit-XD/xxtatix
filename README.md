<p align="center">
  <img src="xxtatix-banner.png" width="600" alt="XXTATIX Banner">
</p>

<h1 align="center">✦ XXTATIX ✦</h1>
<p align="center">⚡ Mini Web Application Security Scanner ⚡</p>
<p align="center">by <b>Amit-XD</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python">
  <img src="https://img.shields.io/github/license/Amit-XD/xxtatix" alt="License">
  <img src="https://img.shields.io/github/last-commit/Amit-XD/xxtatix" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/Amit-XD/xxtatix" alt="Issues">
  <img src="https://img.shields.io/github/stars/Amit-XD/xxtatix?style=social" alt="Stars">
</p>

---

## 📑 Table of Contents
- [✨ Features](#-features)
- [🚀 Installation](#-installation)
- [📖 Usage](#-usage)
- [📊 Examples](#-examples)
- [📂 Project Structure](#-project-structure)
- [⚖️ Legal / Ethics Notice](#️-legal--ethics-notice)
- [📜 License](#-license)

---

## ✨ Features
✔️ Security headers check  
✔️ Reflected XSS detection  
✔️ Open redirect detection  
✔️ Directory & file discovery  
✔️ JSON report output  
✔️ Multi-threaded scanning for speed  

---

## 🚀 Installation

```bash
git clone https://github.com/Amit-XD/xxtatix.git
cd xxtatix
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

📖 Usage

🔹 ### Quick Scan
```bash
python xxtatix.py -u https://example.com


🔹 Save JSON Report
python xxtatix.py -u https://example.com --json report.json

🔹 Custom Wordlist, Payloads & Threads
python xxtatix.py -u https://example.com --wordlist wordlist.txt --payloads payloads.txt --threads 20

🔹 Allow Self-Signed Certs (Labs)
python xxtatix.py -u https://127.0.0.1 --insecure

📊 Examples

╔═══════════════════════════════════════════╗
║          ✦  X X T A T I X  ✦              ║
╚═══════════════════════════════════════════╝

   ⚡ Mini Web Application Security Scanner ⚡
                 by Amit

Target: https://testphp.vulnweb.com

[+] Checking Security Headers...
Headers: 100%|████████| 8/8 [00:00<00:00, ...]
...
[+] No reflected XSS detected with basic payloads.
[+] No open redirects detected with basic probes.
[!] Interesting directories/files found:
   https://testphp.vulnweb.com/robots.txt  [200]

JSON Output Example:
python xxtatix.py -u https://testphp.vulnweb.com --json examples/report.json

📂 Project Structure
xxtatix/
├─ xxtatix.py
├─ payloads.txt
├─ wordlist.txt
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ xxtatix-banner.png   


⚖️ Legal / Ethics Notice

This tool is for educational purposes only.
✅ Use only on assets you own or have explicit permission to test.
❌ Unauthorized use against external systems is illegal.

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

