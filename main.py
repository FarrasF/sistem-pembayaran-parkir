# ============================================================
#  PROGRAM PEMBAYARAN PARKIR - KONSEP OOP LENGKAP (INTERAKTIF)
# ============================================================
from kendaraan import Motor, Mobil          # Inheritance, Abstract, Polymorphism
from pembayaran import Tunai, Digital       # Interface, Overriding, Overloading
from parkir_manager import ParkirManager    # Aggregation, Association

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("   SISTEM PARKIR - MALL ABC")
    print("=" * 40)
    print("  1. Kendaraan Masuk")
    print("  2. Kendaraan Keluar & Bayar")
    print("  3. Lihat Kendaraan Terparkir")
    print("  4. Keluar Program")
    print("-" * 40)

def input_kendaraan():
    print("\n--- KENDARAAN MASUK ---")
    print("  Jenis: 1. Motor  2. Mobil")
    jenis = input("  Pilih [1/2]: ").strip()
    plat = input("  Plat nomor : ").strip().upper()
    pemilik = input("  Pemilik (kosong=Umum): ").strip()
    kelas = {"1": Motor, "2": Mobil}.get(jenis)  # Polymorphism: pilih class saat runtime
    if not kelas:
        print("  [X] Jenis tidak valid!"); return None
    # Constructor + Overloading: dengan/tanpa pemilik (default param)
    return kelas(plat, pemilik) if pemilik else kelas(plat)  # Object creation

def input_keluar(parkir):
    print("\n--- KENDARAAN KELUAR ---")
    plat = input("  Plat nomor: ").strip().upper()
    try: durasi = int(input("  Durasi (jam): ").strip())
    except ValueError: print("  [X] Durasi tidak valid!"); return
    print("  Bayar: 1.Tunai  2.GoPay  3.OVO(diskon 10%)")
    m = input("  Pilih [1/2/3]: ").strip()
    # Polymorphism & Overriding: setiap metode punya implementasi bayar() sendiri
    metode = {"1": Tunai(), "2": Digital("GoPay"), "3": Digital("OVO")}.get(m)  # Object dari Interface
    if not metode:
        print("  [X] Metode tidak valid!"); return
    # Association: ParkirManager menggunakan MetodePembayaran
    # Overloading: diskon=10 jika OVO, diskon=0 jika lainnya
    parkir.kendaraan_keluar(plat, metode, durasi, diskon=10 if m == "3" else 0)

# ---- Program Utama ----
parkir = ParkirManager("Mall ABC")  # Object ParkirManager

while True:
    tampilkan_menu()
    p = input("  Pilih menu [1-4]: ").strip()
    if p == "1":
        k = input_kendaraan()                  # Membuat objek Kendaraan
        if k: parkir.kendaraan_masuk(k)        # Aggregation + Composition
    elif p == "2": input_keluar(parkir)         # Association dengan MetodePembayaran
    elif p == "3":
        print("\n--- KENDARAAN TERPARKIR ---")
        parkir.tampilkan_kendaraan()
    elif p == "4": print("\n  Terima kasih!"); break
    else: print("  [X] Pilihan tidak valid!")
