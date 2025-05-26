#!/usr/bin/env python3
"""
run_all.py – Esegue il ciclo completo:
1. Invia il segnale semantico
2. Genera il report HTML aggiornato
"""

import subprocess

print(">>> Invio segnale con inject_semantic.py")
subprocess.run(["python3", "inject_semantic.py"])

print("\n>>> Generazione report HTML")
subprocess.run(["python3", "generate_report.py"])

print("\n>>> Tutto completato.")
