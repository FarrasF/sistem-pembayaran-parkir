# Interface (Abstract Class murni), Overriding, Overloading
from abc import ABC, abstractmethod

class MetodePembayaran(ABC):  # Interface - semua method abstract (kontrak)
    @abstractmethod
    def bayar(self, jumlah): pass       # Abstract Method
    @abstractmethod
    def nama_metode(self): pass         # Abstract Method

class Tunai(MetodePembayaran):  # Inheritance + Overriding dari Interface
    def bayar(self, jumlah): return f"Bayar tunai: Rp{jumlah:,}"  # Overriding
    def nama_metode(self): return "Tunai"                          # Overriding

class Digital(MetodePembayaran):  # Inheritance + Overriding + Overloading
    def __init__(self, platform="GoPay"):  # Constructor + Overloading (default param)
        self.__platform = platform          # Encapsulation (private)
    def bayar(self, jumlah, diskon=0):  # Overloading via default parameter
        total = int(jumlah - (jumlah * diskon / 100))
        if diskon > 0:
            return f"Bayar via {self.__platform}: Rp{total:,} (diskon {diskon}%)"
        return f"Bayar via {self.__platform}: Rp{total:,}"
    def nama_metode(self): return f"Digital ({self.__platform})"  # Overriding
