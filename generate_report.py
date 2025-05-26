#!/usr/bin/env python3
"""
generate_report.py – Genera un report HTML leggibile
dal file di log 'semantic_log.jsonl' prodotto da inject_semantic.py
"""

from datetime import datetime
import json
from pathlib import Path

# Percorso al file log
log_path = Path("semantic_log.jsonl")

# Output HTML
html_output = Path("thrueads.html")

# Carica le righe JSONL
entries = []
if log_path.exists():
    with open(log_path, "r") as f:
        for line in f:
            try:
                data = json.loads(line)
                timestamp = data.get("timestamp", "N/A")
                targets = data.get("targets", [])
                for domain in targets:
                    entries.append((timestamp, domain))
            except json.JSONDecodeError:
                continue

# Crea il file HTML
html_content = f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>ThrueAds – AdTruth Report</title>
  <style>
    body {{
      background: #111;
      color: #eee;
      font-family: sans-serif;
      padding: 2em;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 2em;
    }}
    th, td {{
      padding: 10px;
      border: 1px solid #444;
      text-align: left;
    }}
    th {{
      background-color: #222;
    }}
    .footer {{
      margin-top: 3em;
      font-size: 0.9em;
      color: #aaa;
    }}
  </style>
</head>
<body>
<h1>ThrueAds – AdTruth Report</h1>
<p>Questo report mostra il risultato del monitoraggio DNS effettuato dal programma <strong>inject_semantic.py</strong>.</p>
<table>
  <tr><th>Timestamp</th><th>Dominio</th></tr>"""

for timestamp, domain in entries:
    html_content += f"\n  <tr><td>{timestamp}</td><td>{domain}</td></tr>"

html_content += f"""
</table>
<div class="footer">
  Ultimo aggiornamento: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
</div>
</body>
</html>
"""

# Scrive l'output
with open(html_output, "w") as f:
    f.write(html_content)

print("✅ File 'thrueads.html' aggiornato con i dati del log.")
