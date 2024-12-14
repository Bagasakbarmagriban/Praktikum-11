class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_biodata(self):
        print(f"\nNama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Angkatan: {self.angkatan}")

    @staticmethod
    def tampilkan_total_mahasiswa():
        print(f"\nTotal Mahasiswa yang Terdaftar: {Mahasiswa.total_mahasiswa}")


if __name__ == "__main__":
    print("Selamat datang di program data mahasiswa\n")
    nama = input("Boleh tau namamu siapa?: ")
    nim = input("Terus, NIM kamu berapa?: ")
    angkatan = input("Oke, angkatan tahun berapa nih?: ")

    mahasiswa = Mahasiswa(nama, nim, angkatan)

    print("\nBerikut biodata yang sudah kamu input:")
    mahasiswa.tampilkan_biodata()

    print("\nDan ini data terakhir:")
    Mahasiswa.tampilkan_total_mahasiswa()
