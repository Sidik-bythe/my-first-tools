# CATATAN D2 - M. Djafar Sidik Indarto
Tanggal: 23 Okt 2026 | HP: Infinix + Termux

## YANG GUE KUASAIN DI D2 (Bukan cuma ngoding)
D2 itu naik level dari D1. D1 manual, D2 otomatis.

### 1. API - Ngambil data dari internet
File: harga.py
Fungsi: Ambil harga XAU/USD live
Skill: requests.get() ke API emas
Hasil: $4028.60 tadi

### 2. Database CSV - Nyimpen history
File: harga.csv
Format: tanggal,jam,harga
Isi: 2026-10-23 19:30:48,4028.60098
Gunanya: Jadi data buat analisa nanti di D3

### 3. CRON - Biar HP kerja sendiri
Perintah: crontab -e
Isi: 0 * * * * ~/my-first-tools/auto-harga.sh
Arti: Tiap jam 00 menit, jalanin auto-harga.sh
Walaupun HP dikunci, bot tetep jalan (kalo Termux:Boot aktif)

### 4. Automation Script
File: auto-harga.sh
Isinya 3 langkah otomatis:
- python harga.py -> ambil harga
- echo ke harga.csv -> simpen
- git add + commit + push -> upload ke GitHub

### 5. Token Classic (Yang bikin pusing tadi)
Link bener: github.com/settings/tokens/new
Note harus beda: termux-d2 (gak boleh sama kayak sebelumnya)
Centang: repo
Kalo error "Catatan sudah diambil" = ganti nama note aja

### BUKTI D2 BERHASIL
- git push keluar: main -> main
- File di GitHub ada: harga.py, auto-harga.sh, harga.csv
- harga.csv nambah sendiri tiap jam

### KENAPA LINGLUNG?
D1 hasilnya langsung keliatan di layar.
D2 hasilnya di belakang layar (cron + auto push). Wajar kalo bingung, tapi ini skill programmer beneran.

NEXT D3: Bikin scalp.py buat sinyal BUY/SELL otomatis dari data harga.csv ini
