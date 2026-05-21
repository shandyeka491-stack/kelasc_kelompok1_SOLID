class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

class HewanTerbang:
    def terbang(self):
        print(f"{self.nama} sedang terbang.")
    

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

class PerawatanKandang:
    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")


class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

class PerawatanHewan:
    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
