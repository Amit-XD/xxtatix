#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xxtatix - Mini Web Application Security Scanner
# Author: Amit
#

import requests
import urllib3
import argparse
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =============================
# Banner
# =============================
def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════════════╗
║          ✦  X X T A T I X  ✦              ║
╚═══════════════════════════════════════════╝
    """)
    print(Fore.MAGENTA + "   ⚡ Mini Web Application Security Scanner ⚡")
    print(Fore.YELLOW + "                 by Amit\n")


# =============================
# Security Headers Check
# =============================
def check_security_headers(url):
    print(Fore.CYAN + "[+] Checking Security Headers...")
    headers_result = {}
    try:
        response = requests.get(url, timeout=10, verify=False)
        for h in tqdm(
            [
                "Content-Security-Policy",
                "Strict-Transport-Security",
                "X-Content-Type-Options",
                "X-Frame-Options",
                "Referrer-Policy",
                "Permissions-Policy",
                "Cross-Origin-Opener-Policy",
                "Cross-Origin-Resource-Policy",
            ],
            desc="Headers",
            colour="green",
        ):
            headers_result[h] = h in response.headers
            time.sleep(0.1)
    except Exception as e:
        print(Fore.RED + f"   Error: {e}")
    return headers_result


# =============================
# XSS Test
# =============================
def test_xss(url, payloads="payloads.txt"):
    print(Fore.CYAN + "[+] Testing for XSS...")
    results = []
    try:
        with open(payloads, "r") as f:
            payload_list = [line.strip() for line in f]

        for payload in tqdm(payload_list, desc="XSS", colour="yellow"):
            test_url = url
            if "?" in url:
                test_url = url + "&test=" + payload
            else:
                test_url = url + "?test=" + payload
            try:
                r = requests.get(test_url, timeout=5, verify=False)
                if payload in r.text:
                    results.append(f"[VULNERABLE] {test_url}")
            except:
                pass
            time.sleep(0.05)
    except FileNotFoundError:
        print(Fore.RED + "   payloads.txt not found!")
    return results


# =============================
# Open Redirect Test
# =============================
def test_open_redirect(url):
    print(Fore.CYAN + "[+] Testing for Open Redirects...")
    results = []
    payloads = [
        "https://evil.com",
        "//evil.com",
        "/\\evil.com",
        "///evil.com",
    ]

    for payload in tqdm(payloads, desc="Redirects", colour="blue"):
        test_url = url
        if "?" in url:
            test_url = url + "&next=" + payload
        else:
            test_url = url + "?next=" + payload
        try:
            r = requests.get(test_url, timeout=5, verify=False, allow_redirects=False)
            if "evil.com" in str(r.headers.get("Location", "")):
                results.append(f"[POSSIBLE REDIRECT] {test_url}")
        except:
            pass
        time.sleep(0.1)
    return results


# =============================
# Directory Bruteforce
# =============================
def dir_bruteforce(url, wordlist="wordlist.txt", threads=10):
    print(Fore.CYAN + "[+] Starting Directory Bruteforce...")
    results = []
    try:
        with open(wordlist, "r") as f:
            paths = [line.strip() for line in f]

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {
                executor.submit(requests.get, urljoin(url, path), timeout=5, verify=False): path
                for path in paths
            }
            for future in tqdm(as_completed(futures), total=len(futures), desc="Dirs", colour="magenta"):
                path = futures[future]
                try:
                    res = future.result()
                    if res.status_code == 200:
                        results.append(f"{urljoin(url, path)}  [200]")
                except:
                    pass
    except FileNotFoundError:
        print(Fore.RED + "   wordlist.txt not found!")
    return results


# =============================
# Main
# =============================
def main():
    print_banner()

    parser = argparse.ArgumentParser(description="xxtatix - Web App Security Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g. https://example.com/)")
    args = parser.parse_args()
    url = args.url

    print(Fore.YELLOW + f"Target: {url}\n")

    # Run checks
    headers = check_security_headers(url)
    print(Fore.GREEN + "\n[Results] Security Headers:")
    for h, present in headers.items():
        print(f"   {h}: {'✅ Present' if present else '❌ Missing'}")

    xss_results = test_xss(url)
    if xss_results:
        print(Fore.RED + "\n[!] XSS Vulnerabilities Found:")
        for r in xss_results:
            print("   " + r)
    else:
        print(Fore.GREEN + "\n[+] No XSS found.")

    redirect_results = test_open_redirect(url)
    if redirect_results:
        print(Fore.RED + "\n[!] Open Redirects Found:")
        for r in redirect_results:
            print("   " + r)
    else:
        print(Fore.GREEN + "\n[+] No Open Redirects found.")

    dir_results = dir_bruteforce(url)
    if dir_results:
        print(Fore.RED + "\n[!] Interesting Directories Found:")
        for r in dir_results:
            print("   " + r)
    else:
        print(Fore.GREEN + "\n[+] No directories found (with current wordlist).")


if __name__ == "__main__":
    main()

