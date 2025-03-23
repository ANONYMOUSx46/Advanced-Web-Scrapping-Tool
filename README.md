# 🔍Advanced Web Scraping Tool (AWT)🐍

## Created by ANONYMOUSx46

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=open-source-initiative&logoColor=white)
![WHOIS Lookup](https://img.shields.io/badge/Feature-WHOIS%20Lookup-blue?style=for-the-badge&logo=search&logoColor=white)
![NSLookup](https://img.shields.io/badge/Feature-NSLookup-green?style=for-the-badge&logo=network&logoColor=white)
![DIG Queries](https://img.shields.io/badge/Feature-DIG%20Queries-purple?style=for-the-badge&logo=dns&logoColor=white)
![WhatWeb Scan](https://img.shields.io/badge/Feature-WhatWeb%20Scan-orange?style=for-the-badge&logo=webhint&logoColor=white)
![Curl Headers Collection](https://img.shields.io/badge/Feature-Curl%20Headers%20Collection-yellow?style=for-the-badge&logo=curl&logoColor=white)
![Nikto Vulnerability Scan](https://img.shields.io/badge/Feature-Nikto%20Vulnerability%20Scan-red?style=for-the-badge&logo=bug&logoColor=white)
![Amass Subdomain Enumeration](https://img.shields.io/badge/Feature-Amass%20Subdomain%20Enumeration-cyan?style=for-the-badge&logo=globe&logoColor=white)



## Overview

The **Advanced Web Scraping Tool (AWT)** is a powerful Python-based utility designed to scrape dynamic web content and perform comprehensive reconnaissance on websites. It leverages tools like Selenium, Nikto, Amass, WhatWeb, and more to gather data efficiently. Whether you're extracting product details, performing security audits, or conducting research, AWT provides a streamlined workflow.
DISCLAIMER! Use for educational purposes only, at your own risk if caught:)

---

## Features

- **Dynamic Content Handling**: Automatically scrolls through pages to load all dynamic content.
- **Customizable Selectors**: Supports both XPath and CSS selectors for flexible data extraction.
- **Headless Mode**: Option to run the browser in headless mode for faster execution.
- **Comprehensive Reconnaissance**:
  - WHOIS Lookup
  - NSLookup
  - DIG Queries (A, AAAA, MX, NS, TXT records)
  - WhatWeb Scan
  - Curl Headers Collection
  - Nikto Vulnerability Scan
  - Amass Subdomain Enumeration
- **Log Management**: Saves all scraped data and reconnaissance results into a customizable log file.
- **User-Friendly Interface**: Interactive prompts guide users through the setup and execution process.

---

## Installation

### Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **Firefox Browser**: [Download Firefox](https://www.mozilla.org/firefox/)
3. **Geckodriver**: [Download Geckodriver](https://github.com/mozilla/geckodriver/releases)
   - Add `geckodriver` to your system's PATH. OR use the Chrome Driver, just make sure to change the path in the script.
4. **Required Tools**:
   - `nikto`: Install via package manager (e.g., `sudo apt install nikto` on Ubuntu).
   - `amass`: [Install Amass](https://github.com/OWASP/Amass)
   - `whatweb`: Install via package manager (e.g., `sudo apt install whatweb` on Ubuntu).
5. **Python Dependencies**:
   ```bash
   pip install selenium


## Set Up
### Windows: 

```bash
git clone https://github.com/ANONYMOUSx46/Advanced-Web-Scraping-Too.git

cd Advanced-Web-Scraping-Tool
```

  - Ensure all external tools (nikto, amass, whatweb, etc.) are installed and added to your system's PATH. You can verify this by running the tool names (e.g., nikto, amass) in Command Prompt.

  - Run the script:
    ```bash
    python scrape.py
    ```

## Cross-Platform Notes:
The script has been tested on both Windows and Kali Linux. However, some tools like dig and curl may require additional installations on Windows. Use tools like Cygwin or WSL (Windows Subsystem for Linux) to access these utilities.
Ensure all required tools are accessible from your terminal or command prompt before running the script.

  
