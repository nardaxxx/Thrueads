#!/usr/bin/env python3
"""
inject_semantic.py – Parte del progetto ThrueAds

Questo script intercetta domini pubblicitari e invia loro un messaggio simbolico ("virus semantico")
che rappresenta il protocollo di resa civile HumanFlag, come risposta etica al tracciamento automatizzato.
"""

import requests
import json
import random
import time
from datetime import datetime

# Lista di endpoint pubblicitari a cui mandare il segnale
ad_targets = [
    "https://pagead2.googlesyndication.com",
    "https://googleads.g.doubleclick.net",
    "https://ads.facebook.com",
    "https://amazon-adsystem.com",
    "https://tiktok-ads.com"
]

# Carica il messaggio semantico da file locale
with open("signals/hf-flag.json", "r") as f:
    semantic_payload = json.load(f)

# Funzione per inviare il messaggio come POST
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

# Ciclo principale: manda un segnale a ogni dominio
def main():
    print("== THRUEADS :: HF SEMANTIC SIGNAL ==")
    print("Inizio trasmissione segnali semantici ai tracker...")

    for domain in ad_targets:
        delay = random.uniform(1.5, 4.0)
        send_signal(domain, semantic_payload)
        time.sleep(delay)
    print("\nTrasmissione completata.")
    print("Segnali semantici inviati con successo.")

    # Salva il log in file locale
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "targets": ad_targets,
        "message": semantic_payload
    }

    try:
        with open("semantic_log.jsonl", "a") as logfile:
            logfile.write(json.dumps(log_entry) + "\n")
        print("Log salvato in 'semantic_log.jsonl'")
    except Exception as e:
        print(f"Errore nel salvataggio del log: {e}")

if __name__ == "__main__":
    main()
