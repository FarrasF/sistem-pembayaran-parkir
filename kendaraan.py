# Abstract Class, Inheritance, Encapsulation, Polymorphism, Overriding
from abc import ABC, abstractmethod

class Kendaraan(ABC):  # Abstract Class - tidak bisa diinstansiasi langsung
    def __init__(self, plat_nomor, pemilik="Umum"):  # Constructor + Overloading (default param)
        self.__plat_nomor = plat_nomor  # Encapsulation (private attribute)
        self.__pemilik = pemilik        # Encapsulation (private attribute)

    def get_plat_nomor(self): return self.__plat_nomor  # Getter (Encapsulation)
    def get_pemilik(self): return self.__pemilik        # Getter (Encapsulation)

    @abstractmethod
    def hitung_tarif(self, durasi): pass  # Abstract Method
    @abstractmethod
    def jenis(self): pass                # Abstract Method

class Motor(Kendaraan):  # Inheritance dari Kendaraan
    TARIF = 2000  # Atribut class
    def __init__(self, plat, pemilik="Umum"):  # Constructor + Overloading
        super().__init__(plat, pemilik)         # Memanggil constructor parent
    def hitung_tarif(self, durasi): return self.TARIF * durasi  # Overriding abstract method
    def jenis(self): return "Motor"  # Overriding + Polymorphism

class Mobil(Kendaraan):  # Inheritance dari Kendaraan
    TARIF = 5000  # Atribut class
    def __init__(self, plat, pemilik="Umum"):  # Constructor + Overloading
        super().__init__(plat, pemilik)         # Memanggil constructor parent
    def hitung_tarif(self, durasi): return self.TARIF * durasi  # Overriding abstract method
    def jenis(self): return "Mobil"  # Overriding + Polymorphism
