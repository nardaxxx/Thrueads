import datetime
import csv

# Lista base di domini pubblicitari noti
ad_domains = [
    "googleads.g.doubleclick.net",
    "pagead2.googlesyndication.com",
    "ads.facebook.com",
    "tiktok-ads.com",
    "amazon-adsystem.com"
]

# Simulazione: domini pari vengono bloccati, dispari no (placeholder per DNS check vero)
dns_results = [
    {"domain": domain, "status": "BLOCKED" if i % 2 == 0 else "ALLOWED"}
    for i, domain in enumerate(ad_domains)
]

# Log su file CSV con timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
filename = f"adtruth_log_{timestamp}.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["timestamp", "domain", "status"])
    writer.writeheader()
    for result in dns_results:
        writer.writerow({
            "timestamp": datetime.datetime.now().isoformat(),
            "domain": result["domain"],
            "status": result["status"]
        })

print(f"[OK] Log creato: {filename}")
