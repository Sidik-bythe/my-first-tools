import csv
from datetime import date
file = "/data/data/com.termux/files/home/my-first-tools/harga.csv"
today = str(date.today())
rows=[]
try:
 with open(file) as f:
  r=csv.DictReader(f)
  for row in r:
   if today in row['waktu']:
    rows.append(row)
except: pass
if len(rows)<3:
 print(f"Data baru {len(rows)} candle, tunggu bentar")
 exit()
harga=[float(x['harga']) for x in rows]
close_h=harga[-1]
prev_h=harga[-2]
sma3=sum(harga[-3:])/3
if close_h>sma3 and close_h>prev_h:
 sig="BUY / LONG"; trend="MOMENTUM NAIK - Rebound ke 4044"
elif close_h<sma3 and close_h<prev_h:
 sig="SELL / SHORT"; trend="MOMENTUM TURUN"
else:
 sig="WAIT"; trend="SIDEWAYS"
print(f"--- SCALP D3 SIDOARJO {today} ---")
print(f"Now: {close_h} | SMA3: {sma3:.2f}")
print(f"=== SINYAL: {sig} ===")
print(f"Trend: {trend}")
print(f"Jarak ke 4044: {4044-close_h:.2f}$")
