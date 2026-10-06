"""
status_mahasiswa.py
Program Penentuan Status Akademik Mahasiswa
===========================================
Modul Praktikum Pemrograman Python - Soal 1
"""

def tentukan_status(ipk: float, sks: int) -> str:
    """
    Menentukan status akademik mahasiswa berdasarkan IPK dan SKS:
    - Aktif: IPK >= 2.0 dan SKS >= 18
    - Peringatan: 1.5 <= IPK < 2.0 (atau IPK >= 2.0 tetapi SKS < 18)
    - Tidak Aktif: IPK < 1.5
    """
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    elif ipk >= 1.5:
        return "Peringatan"
    else:
        return "Tidak Aktif"


def input_data_mahasiswa(jumlah: int = 5) -> list[dict]:
    """Menerima input data n mahasiswa secara interaktif."""
    daftar_mhs = []
    print(f"\n=== INPUT DATA {jumlah} MAHASISWA ===")
    
    for i in range(1, jumlah + 1):
        print(f"\nData Mahasiswa ke-{i}:")
        nim = input("  NIM       : ").strip()
        nama = input("  Nama      : ").strip()
        
        while True:
            try:
                ipk = float(input("  IPK (0.0-4.0): "))
                if 0.0 <= ipk <= 4.0:
                    break
                print("  [Error] IPK harus di antara 0.00 dan 4.00!")
            except ValueError:
                print("  [Error] Masukkan angka desimal yang valid untuk IPK!")

        while True:
            try:
                sks = int(input("  SKS       : "))
                if 0 <= sks <= 24:
                    break
                print("  [Error] SKS harus di antara 0 dan 24!")
            except ValueError:
                print("  [Error] Masukkan angka bulat yang valid untuk SKS!")

        daftar_mhs.append({
            "nim": nim,
            "nama": nama,
            "ipk": ipk,
            "sks": sks
        })
        
    return daftar_mhs


def tampilkan_laporan(daftar_mhs: list[dict]):
    """Menampilkan laporan status akademik dalam bentuk tabel."""
    print("\n" + "=" * 65)
    print(f"{'LAPORAN STATUS AKADEMIK MAHASISWA':^65}")
    print("=" * 65)
    print(f"{'NO':<4} {'NIM':<12} {'NAMA MAHASISWA':<22} {'IPK':>6} {'SKS':>5} {'STATUS':<12}")
    print("-" * 65)
    
    for idx, mhs in enumerate(daftar_mhs, start=1):
        status = tentukan_status(mhs["ipk"], mhs["sks"])
        print(f"{idx:<4} {mhs['nim']:<12} {mhs['nama']:<22} {mhs['ipk']:>6.2f} {mhs['sks']:>5} {status:<12}")
        
    print("=" * 65)


def get_sample_data() -> list[dict]:
    """Menyediakan sampel data 5 mahasiswa untuk pengujian otomatis."""
    return [
        {"nim": "2023001001", "nama": "Andi Pratama", "ipk": 3.65, "sks": 21},
        {"nim": "2023001002", "nama": "Budi Santoso", "ipk": 1.85, "sks": 16},
        {"nim": "2023001003", "nama": "Citra Dewi", "ipk": 1.20, "sks": 12},
        {"nim": "2023001004", "nama": "Dian Wijaya", "ipk": 2.50, "sks": 15},
        {"nim": "2023001005", "nama": "Eka Saputra", "ipk": 3.90, "sks": 24},
    ]


def main():
    print("=== PROGRAM LAPORAN STATUS MAHASISWA ===")
    print("1. Input Manual Data 5 Mahasiswa")
    print("2. Gunakan Data Sampel (Demonstrasi Cepat)")
    pilihan = input("Pilih mode (1/2) [Default 1]: ").strip()
    
    if pilihan == "2":
        daftar_mhs = get_sample_data()
        print("\n[INFO] Menggunakan data sampel 5 mahasiswa.")
    else:
        daftar_mhs = input_data_mahasiswa(5)
        
    tampilkan_laporan(daftar_mhs)


if __name__ == "__main__":
    main()
