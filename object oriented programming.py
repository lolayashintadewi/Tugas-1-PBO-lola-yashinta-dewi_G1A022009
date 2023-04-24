class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def get_nama(self):
        return self.nama

    def get_npm(self):
        return self.npm

# Penggunaan kelas
mhs = Mahasiswa("Lola Yashinta Dewi", "G1A022009")
print("Nama:", mhs.get_nama())
print("NPM:", mhs.get_npm())
