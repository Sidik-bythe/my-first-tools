import csv, os, json
from datetime import datetime, date
import urllib.request

file_harga = os.path.expanduser("~/my-first-tools/harga.csv")
file_log = os.path.expanduser("~/my-first-tools/sinyal.log")

# ambil harga GC=F langsung tanpa yfinance
url = "https://query1.finance.yahoo.com/v8/finance/chart/GC=F?interval=1m&range=1d"
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        j = json.loads(r.read().decode())
        price = j['chart']['result'][0]['meta']['regularMarketPrice']
except Exception as e:
    print(f"Gagal ambil harga: {e}")
    exit()

now = datetime.now().strftime("%Y-%m-%d %H:%M")
header = not os.path.exists(file_harga)
with open(file_harga, "a", newline="") as f:
    w = csv.writer(f)
    if header: w.writerow(["waktu","harga"])
    w.writerow([now, price])

today = str(date.today())
rows = []
if os.path.exists(file_harga):
    with open(file_harga) as f:
        for r in csv.DictReader(f):
            if today in r['waktu']:
                rows.append(r)

if len(rows) >= 3:
    h = [float(x['harga']) for x in rows]
    close_h, prev_h = h[-1], h[-2]
    sma3 = sum(h[-3:])/3
    if close_h > sma3 and close_h > prev_h:
        sig = "BUY"
    elif close_h < sma3 and close_h < prev_h:
        sig = "SELL"
    else:
        sig = "WAIT"
    pesan = f"{now} | {close_h:.2f} | SMA:{sma3:.1f} | {sig}"
    print(pesan)
    with open(file_log, "a") as f:
        f.write(pesan + "\n")
else:
    print(f"Data baru {len(rows)} | Harga {price:.2f} | tunggu 3 candle")
