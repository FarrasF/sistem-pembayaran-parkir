# Aggregation & Association
# - Aggregation: ParkirManager 'mengumpulkan' TiketParkir (tiket bisa ada tanpa manager)
# - Association: ParkirManager 'menggunakan' MetodePembayaran saat proses keluar
from tiket import TiketParkir

class ParkirManager:  # Aggregation + Association
    def __init__(self, nama_lokasi):       # Constructor
        self.__nama_lokasi = nama_lokasi   # Encapsulation (private)
        self.__tiket_aktif = {}            # Aggregation: dict plat -> TiketParkir

    def get_nama_lokasi(self): return self.__nama_lokasi  # Getter (Encapsulation)

    def kendaraan_masuk(self, kendaraan):  # Method
        plat = kendaraan.get_plat_nomor()
        if plat in self.__tiket_aktif:
            print(f"  [X] {plat} sudah terdaftar!"); return None
        tiket = TiketParkir(kendaraan)     # Composition di dalam TiketParkir
        self.__tiket_aktif[plat] = tiket   # Aggregation: menyimpan tiket
        print(f"  [V] {tiket}"); return tiket

    def kendaraan_keluar(self, plat, metode, durasi=2, diskon=0):  # Association + Overloading
        """Association: menerima objek MetodePembayaran dari luar"""
        if plat not in self.__tiket_aktif:
            print(f"  [X] {plat} tidak ditemukan!"); return
        tiket = self.__tiket_aktif.pop(plat)
        biaya = tiket.hitung_biaya(durasi)  # Polymorphism: tarif tergantung jenis kendaraan
        print(f"  Kendaraan : {tiket.get_kendaraan().jenis()} [{plat}]")
        print(f"  Durasi    : {durasi} jam")
        print(f"  Biaya     : Rp{biaya:,}")
        if diskon > 0:
            print(f"  {metode.bayar(biaya, diskon=diskon)}")  # Overloading bayar(jumlah, diskon)
        else:
            print(f"  {metode.bayar(biaya)}")  # Association: menggunakan metode pembayaran

    def tampilkan_kendaraan(self):  # Method
        if not self.__tiket_aktif:
            print("  (Parkiran kosong)"); return
        for tiket in self.__tiket_aktif.values():
            print(f"  {tiket}")
