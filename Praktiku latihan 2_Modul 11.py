class Mahasiswa:

    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    @property
    def info(self):
        return "Nama: {} \nNilai: {}".format(self.nama, self.__nilai)

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai_baru):
        self.__nilai = nilai_baru

    @nilai.deleter
    def nilai(self):
        self.__nilai = None


def main():
    mahasiswa = Mahasiswa(None, None)
    keluar_program = False
    
    while not keluar_program:
        print('===== Program OOP =====')
        print('1. Deklarasi Objek',
              '\n2. Tampilkan Objek',
              '\n3. Ubah Data Objek',
              '\n4. Hapus Data Objek',
              '\n5. Keluar Program\n')
        
        pilihan = int(input("Masukkan pilihan Anda (1/2/3/4/5): "))
        
        if pilihan == 1:
            nama = input("Masukkan namamu: ")
            nilai = int(input("Masukkan nilaimu: "))
            mahasiswa = Mahasiswa(nama, nilai)
            print("Data berhasil ditambahkan.\n")
        
        elif pilihan == 2:
            print("\n" + mahasiswa.info + "\n")
        
        elif pilihan == 3:
            opsi = input("Apa yang ingin diubah (Nama/Nilai): ").lower()
            if opsi == "nama":
                nama = input("Masukkan nama baru: ")
                mahasiswa.nama = nama
                print("Nama berhasil diubah.\n")
            elif opsi == "nilai":
                nilai = int(input("Masukkan nilai baru: "))
                mahasiswa.nilai = nilai
                print("Nilai berhasil diubah.\n")
            else:
                print("Pilihan tidak valid! Pilih Nama atau Nilai.\n")
        
        elif pilihan == 4:
            mahasiswa.nama = None
            del mahasiswa.nilai
            print("Data berhasil dihapus.\n")
        
        elif pilihan == 5:
            print("Terima kasih telah menggunakan program ini.")
            keluar_program = True
        
        else:
            print("Input tidak valid! Silakan coba lagi.\n")


main()
