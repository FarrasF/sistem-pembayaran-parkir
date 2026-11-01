# Composition - TiketParkir MEMILIKI Kendaraan (jika tiket dihapus, relasi ikut hilang)
from datetime import datetime

class TiketParkir:  # Composition: TiketParkir 'memiliki' objek Kendaraan
    _counter = 0    # Class attribute untuk ID unik

    def __init__(self, kendaraan):       # Constructor - Composition (menerima objek Kendaraan)
        TiketParkir._counter += 1
        self.__id = TiketParkir._counter  # Encapsulation (private)
        self.__kendaraan = kendaraan      # Composition: kendaraan menjadi bagian dari tiket
        self.__waktu_masuk = datetime.now()  # Encapsulation (private)

    def get_id(self): return self.__id               # Getter (Encapsulation)
    def get_kendaraan(self): return self.__kendaraan  # Getter (Encapsulation)
    def get_waktu_masuk(self): return self.__waktu_masuk

    def hitung_durasi(self):  # Method
        return max(1, int((datetime.now() - self.__waktu_masuk).total_seconds() / 3600) + 1)

    def hitung_biaya(self, durasi=None):  # Overloading via default parameter
        return self.__kendaraan.hitung_tarif(durasi or self.hitung_durasi())  # Polymorphism

    def __str__(self):  # Overriding method bawaan Python (__str__)
        k = self.__kendaraan
        return (f"[Tiket #{self.__id}] {k.jenis()} | Plat: {k.get_plat_nomor()} | "
                f"Pemilik: {k.get_pemilik()} | Masuk: {self.__waktu_masuk:%H:%M:%S}")
