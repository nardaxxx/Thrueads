#!/usr/bin/env python3
"""
inject_semantic.py – ThrueAds / HumanFlag

Controlla se la tua rete raggiunge i server pubblicitari.
E, se vuoi, invia un messaggio simbolico di resa civile (HF-SIGNAL)
e lo registra per generare un report.
"""

import requests
import json
import random
import time
import socket
import argparse
from datetime import datetime

# Domini pubblicitari da verificare o "infettare"
ad_targets = [
    "googleads.g.doubleclick.net",
    "pagead2.googlesyndication.com",
    "ads.facebook.com",
    "amazon-adsystem.com",
    "tiktok-ads.com"
]

# Carica il messaggio HF dal file locale
with open("signals/hf-flag.json", "r", encoding="utf-8") as f:
    semantic_payload = json.load(f)

# === Modalità 1: Controlla DNS (reale) ===
def check_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        return "ALLOWED", ip
    except Exception:
        return "BLOCKED", None

def dns_check():
    print("== DNS CHECK :: Verifica accesso a server pubblicitari ==")
    for domain in ad_targets:
        status, ip = check_dns(domain)
        print(f"{domain}: {status} ({ip if ip else 'N/A'})")

# === Modalità 2: Invia segnale ===
def send_signal(target_url, payload):
    headers = {
        "User-Agent": "HumanFlag/1.0",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(target_url, json=payload, headers=headers, timeout=5)
        print(f"[{datetime.now().isoformat()}] -> {target_url} | STATUS: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] -> {target_url} | ERROR: {str(e)}")

def transmit_signal():
    print("== THRUEADS :: HF SEMANTIC SIGNAL ==")
    print("Inizio trasmissione ai tracker...")

    for domain in ad_targets:
        delay = random.uniform(1.5, 3.5)
        send_signal(f"https://{domain}", semantic_payload)
        time.sleep(delay)

    print("Trasmissione completata.")

    # Salva il log
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "targets": ad_targets,
        "message": semantic_payload
    }

    try:
        with open("semantic_log.jsonl", "a", encoding="utf-8") as logfile:
            logfile.write(json.dumps(log_entry) + "\n")
        print("Log salvato in 'semantic_log.jsonl'")
    except Exception as e:
        print(f"Errore nel salvataggio log: {e}")

# === Main CLI ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ThrueAds – Semantic DNS + Signal Tool")
    parser.add_argument("--check", action="store_true", help="Controlla accessibilità DNS (senza inviare)")
    args = parser.parse_args()

    if args.check:
        dns_check()
    else:
        transmit_signal()
