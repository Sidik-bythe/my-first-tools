import requests, csv
from datetime import datetime
try:
    r = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
    harga = r.get('price', 0)
except:
    harga = 0
waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{waktu} - Emas: ${harga}")
with open("harga.csv", "a", newline="") as f:
    import csv
    csv.writer(f).writerow([waktu, harga])
