# Contoh kelas untuk merepresentasikan karyawan
class Karyawan:
    def _init_(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def naik_gaji(self, persentase):
        self.gaji += (self.gaji * persentase / 100)

# Contoh pembuatan objek dari kelas Karyawan
karyawan1 = Karyawan("Agus", "Manager", 10000000)
karyawan2 = Karyawan("Budi", "Programmer", 5000000)

# Memanggil method pada objek
print("Gaji karyawan1 sebelum naik gaji:", karyawan1.gaji)
karyawan1.naik_gaji(10)
print("Gaji karyawan1 setelah naik gaji:", karyawan1.gaji)
