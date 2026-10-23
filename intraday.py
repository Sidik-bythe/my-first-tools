import csv
from datetime import date
today = str(date.today())
file = "/data/data/com.termux/files/home/my-first-tools/harga.csv"

try:
    rows = []
    with open(file) as f:
        r = csv.DictReader(f)
        for row in r:
            if today in row['waktu']:
                rows.append(row)
    if not rows:
        print(f"Belum ada data {today}")
    else:
        harga = [float(x['harga']) for x in rows]
        open_h = harga[0]
        close_h = harga[-1]
        high = max(harga)
        low = min(harga)
        chg = close_h - open_h
        print(f"--- INTRADAY {today} ---")
        print(f"Data: {len(rows)} candle")
        print(f"Open: {open_h}")
        print(f"High: {high}")
        print(f"Low: {low}")
        print(f"Now: {close_h}")
        print(f"Change: {chg:.2f} ({chg/open_h*100:.2f}%)")
        print(f"Jarak ke 4066: {4066-close_h:.2f}$")
        if close_h < 4044:
            print("Trend: MASIH BEARISH di bawah 4044")
        else:
            print("Trend: MULAI REBOUND menuju 4066!")
        print("\nDetail:")
        for x in rows[-10:]:
            print(f"{x['waktu']} -> {x['harga']}")
except Exception as e:
    print(e)
