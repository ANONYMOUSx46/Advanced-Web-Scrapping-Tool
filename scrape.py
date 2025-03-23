import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

def display_banner():
    """
    Display the ASCII art banner for the tool.
    """
    banner = r"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░              ║
║   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                 ║
║   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                 ║
║   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                 ║
║   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                 ║
║   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                 ║
║   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█████████████▓▒░   ░▒▓█▓▒░                 ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
        🐍🔍 Advanced Web Scrapping Tool (AWT) 🔍🐍
               Created by: ANONYMOUSx46
                "Empowering Web Recon"
        Tools Integrated: WHOIS, NSLookup, DIG, WhatWeb,
                          Nikto, Amass, Selenium Scraping
    """
    print(banner)

def get_user_input():
    """
    Prompt the user for input: URL, XPath/CSS selectors, headless mode, Nikto settings, and log file name.
    """
    url = input("Enter the URL of the website you want to scrape: ")
    selector_type = input("Choose selector type (XPath or CSS): ").strip().lower()
    if selector_type not in ["xpath", "css"]:
        print("Invalid selector type. Defaulting to XPath.")
        selector_type = "xpath"
    container_selector = input("Enter the selector for the container element (e.g., '//div[@class=\"product\"]'): ")
    title_selector = input("Enter the selector for the title element (e.g., '.title' or './/h2'): ")
    price_selector = input("Enter the selector for the price element (e.g., '.price' or './/span[@class=\"price\"]'): ")
    headless_mode = input("Run in headless mode? (yes/no): ").strip().lower() == "yes"
    skip_nikto = input("Skip Nikto scan? (yes/no): ").strip().lower() == "yes"
    nikto_timeout = input("Enter Nikto scan timeout (e.g., 5m for 5 minutes, or leave blank for default 5m): ").strip()
    nikto_timeout = nikto_timeout if nikto_timeout else "5m"  # Default to 5 minutes
    log_filename = input("Enter a name for your log file (leave blank for default 'scraplogs.txt'): ").strip()
    log_filename = log_filename if log_filename else "scraplogs.txt"
    return url, selector_type, container_selector, title_selector, price_selector, headless_mode, skip_nikto, nikto_timeout, log_filename

def initialize_driver(headless_mode):
    """
    Initialize the Firefox WebDriver with optional headless mode.
    """
    options = Options()
    if headless_mode:
        options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver

def scroll_to_load_content(driver):
    """
    Scroll down the page to load dynamic content until no more content is loaded.
    """
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extract_data(driver, selector_type, container_selector, title_selector, price_selector, log_file):
    """
    Extract data from the webpage using the provided selectors and save it to the log file.
    """
    log_file.write("\n--- Scraped Data ---\n")
    try:
        if selector_type == "xpath":
            containers = driver.find_elements(By.XPATH, container_selector)
        else:
            containers = driver.find_elements(By.CSS_SELECTOR, container_selector)
        for container in containers:
            try:
                if selector_type == "xpath":
                    title_element = container.find_element(By.XPATH, title_selector)
                    price_element = container.find_element(By.XPATH, price_selector)
                else:
                    title_element = container.find_element(By.CSS_SELECTOR, title_selector)
                    price_element = container.find_element(By.CSS_SELECTOR, price_selector)
                title = title_element.text.strip()
                price = price_element.text.strip()
                log_file.write(f"Title: {title}\n")
                log_file.write(f"Price: {price}\n")
                log_file.write("-" * 40 + "\n")
            except Exception as e:
                log_file.write(f"An error occurred while extracting data: {e}\n")
    except Exception as e:
        log_file.write(f"An error occurred during scraping: {e}\n")

def whois_lookup(domain, log_file):
    """
    Perform a WHOIS lookup on the domain and save the results to the log file.
    """
    log_file.write("\n--- WHOIS Lookup ---\n")
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during WHOIS lookup: {e}\n")

def nslookup(domain, log_file):
    """
    Perform an NSLookup to gather DNS information and save the results to the log file.
    """
    log_file.write("\n--- NSLookup ---\n")
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during NSLookup: {e}\n")

def dig_query(domain, record_type, log_file):
    """
    Perform a DIG query to gather specific DNS records and save the results to the log file.
    """
    log_file.write(f"\n--- DIG Query for {record_type} Records ---\n")
    try:
        result = subprocess.run(["dig", domain, record_type], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during DIG query: {e}\n")

def whatweb_scan(url, log_file):
    """
    Perform a WhatWeb scan to gather information about the website and save the results to the log file.
    """
    log_file.write("\n--- WhatWeb Scan ---\n")
    try:
        result = subprocess.run(["whatweb", url], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during WhatWeb scan: {e}\n")

def curl_headers(url, log_file):
    """
    Collect web headers using curl -i and save the results to the log file.
    """
    log_file.write("\n--- Web Headers (curl -i) ---\n")
    try:
        result = subprocess.run(["curl", "-i", url], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during curl headers collection: {e}\n")

def nikto_scan(url, skip_nikto, nikto_timeout, log_file):
    """
    Perform a Nikto scan to identify vulnerabilities and save the results to the log file.
    """
    if skip_nikto:
        log_file.write("\n--- Nikto Scan ---\nSkipping Nikto Scan as requested.\n")
        return
    log_file.write("\n--- Nikto Scan ---\nPerforming Nikto Scan...\n")
    try:
        print("Starting Nikto scan. This may take some time...")
        result = subprocess.run(
            ["nikto", "-h", url, "-Plugins", "default", "-maxtime", nikto_timeout],
            capture_output=True,
            text=True
        )
        log_file.write(result.stdout)
        print("Nikto scan completed.")
    except Exception as e:
        log_file.write(f"Error during Nikto scan: {e}\n")
        print(f"An error occurred during Nikto scan: {e}")

def amass_enum(domain, log_file):
    """
    Perform an Amass enumeration to discover subdomains and save the results to the log file.
    """
    log_file.write("\n--- Amass Enumeration ---\n")
    try:
        result = subprocess.run(["amass", "enum", "-d", domain], capture_output=True, text=True)
        log_file.write(result.stdout)
    except Exception as e:
        log_file.write(f"Error during Amass enumeration: {e}\n")

def decode_headers(log_file):
    """
    Decode headers from a log file into a cleaner format.
    """
    log_file.write("\n--- Decoded HTTP Headers ---\n")
    header_lines = []
    try:
        with open("headers_log.txt", "r") as headers_log:
            header_lines = headers_log.readlines()
        
        cleaned_headers = {}
        for line in header_lines:
            if ":" in line:
                key, value = line.split(":", 1)
                cleaned_headers[key.strip()] = value.strip()
        
        for key, value in cleaned_headers.items():
            log_file.write(f"{key}: {value}\n")
    except FileNotFoundError:
        log_file.write("No headers_log.txt file found. Please run the main script first to collect headers.\n")
    except Exception as e:
        log_file.write(f"Error decoding headers: {e}\n")

def main():
    """
    Main function to orchestrate the web scraping and reconnaissance process.
    """
    display_banner()

    # Display options to the user
    print("\nSelect an option:")
    print("1. Run full reconnaissance and scraping")
    print("2. Perform WHOIS scan only")
    print("3. Decode HTTP headers from previous runs")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        # Run the original script
        (
            url,
            selector_type,
            container_selector,
            title_selector,
            price_selector,
            headless_mode,
            skip_nikto,
            nikto_timeout,
            log_filename,
        ) = get_user_input()

        domain = url.split("//")[-1].split("/")[0]
        if not log_filename.endswith(".txt"):
            log_filename += ".txt"

        with open(log_filename, "w") as log_file:
            log_file.write(f"--- Reconnaissance and Scraping Report for {url} ---\n")
            whois_lookup(domain, log_file)
            nslookup(domain, log_file)
            dig_query(domain, "A", log_file)
            dig_query(domain, "AAAA", log_file)
            dig_query(domain, "MX", log_file)
            dig_query(domain, "NS", log_file)
            dig_query(domain, "TXT", log_file)
            whatweb_scan(url, log_file)
            curl_headers(url, log_file)
            nikto_scan(url, skip_nikto, nikto_timeout, log_file)
            amass_enum(domain, log_file)

            driver = initialize_driver(headless_mode)
            try:
                driver.get(url)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
                scroll_to_load_content(driver)
                extract_data(driver, selector_type, container_selector, title_selector, price_selector, log_file)
            except Exception as e:
                log_file.write(f"\nAn error occurred during scraping: {e}\n")
            finally:
                driver.quit()

        print(f"All data has been saved to '{log_filename}'.")

    elif choice == "2":
        # Perform WHOIS scan only
        domain = input("Enter the domain name for WHOIS lookup: ").strip()
        log_filename = input("Enter the name for the WHOIS log file (default 'whois_log.txt'): ").strip()
        log_filename = log_filename if log_filename else "whois_log.txt"

        with open(log_filename, "w") as log_file:
            whois_lookup(domain, log_file)

        print(f"WHOIS data has been saved to '{log_filename}'.")

    elif choice == "3":
        # Decode HTTP headers
        log_filename = input("Enter the name for the decoded headers log file (default 'decoded_headers.txt'): ").strip()
        log_filename = log_filename if log_filename else "decoded_headers.txt"

        with open(log_filename, "w") as log_file:
            decode_headers(log_file)

        print(f"Decoded headers have been saved to '{log_filename}'.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
