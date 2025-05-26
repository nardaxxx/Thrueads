#!/usr/bin/env python3
"""
inject_semantic.py – Parte del progetto ThrueAds

Questo script invia un messaggio simbolico ("virus semantico") ai domini pubblicitari,
secondo il protocollo HF Vision. È un'azione di disobbedienza etica contro il tracciamento
automatizzato e la guerra algoritmica.

Autore: humanflag.org / thrueads
"""

import requests
import json
import random
import time
import os
from datetime import datetime

# Lista dei domini pubblicitari obiettivo
ad_targets = [
    "https://pagead2.googlesyndication.com",
    "https://googleads.g.doubleclick.net",
    "https://ads.facebook.com",
    "https://amazon-adsystem.com",
    "https://tiktok-ads.com"
]

# Percorso al segnale semantico
payload_path = "signals/hf-flag-signal_1.json"

# Verifica esistenza file
if not os.path.exists(payload_path):
    print(f"[ERRORE] File non trovato: {payload_path}")
    exit(1)

# Carica il messaggio semantico
with open(payload_path, "r", encoding="utf-8") as f:
    semantic_payload = json.load(f)

# Invia il segnale a un dominio
def send_signal(target_url, payload):
    headers = {
        "User-Agent": "HumanFlag/1.0",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(target_url, json=payload, headers=headers, timeout=5)
        print(f"[{datetime.now().isoformat()}] -> {target_url} | STATUS: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] -> {target_url} | ERRORE: {str(e)}")

# Main loop
def main():
    print("== THRUEADS :: HF SEMANTIC SIGNAL ==")
    print("Inizio trasmissione segnali semantici...\n")

    for domain in ad_targets:
        delay = random.uniform(1.5, 4.0)
        send_signal(domain, semantic_payload)
        time.sleep(delay)

    print("\nTrasmissione completata. Log in corso...")

    # Log della sessione
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

if __name__ == "__main__":
    main()
