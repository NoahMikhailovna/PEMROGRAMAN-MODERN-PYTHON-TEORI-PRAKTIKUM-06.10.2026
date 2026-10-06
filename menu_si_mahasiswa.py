"""
menu_si_mahasiswa.py
Aplikasi Sistem Informasi Mahasiswa - Menu Interaktif Integratif
===============================================================
Modul Praktikum Pemrograman Python - Soal 4
"""

import sys
import status_mahasiswa
import diskon_biaya
import peringatan_stok
import validasi_data


def submenu_cek_status_mahasiswa():
    """Submenu (1): Cek Status Mahasiswa."""
    print("\n" + "=" * 60)
    print(f"{'SUBMENU 1: CEK STATUS AKADEMIK MAHASISWA':^60}")
    print("=" * 60)
    print(" 1. Cek Status Individual Mahasiswa")
    print(" 2. Tampilkan Laporan Batch (5 Mahasiswa)")
    print(" 0. Kembali ke Menu Utama")
    
    pilihan = input("\nPilih opsi (1/2/0): ").strip()
    
    if pilihan == "1":
        print("\n--- Input Data Mahasiswa ---")
        
        # Validasi Input NIM
        while True:
            nim = input("Masukkan NIM (10 digit): ").strip()
            err_nim = validasi_data.validasi_nim(nim)
            if not err_nim:
                break
            print(f"  [Error] {err_nim[0]}")
            
        nama = input("Masukkan Nama          : ").strip()
        
        # Validasi Input IPK
        while True:
            ipk_str = input("Masukkan IPK (0.0-4.0) : ").strip()
            val_ipk, err_ipk = validasi_data.validasi_ipk(ipk_str)
            if not err_ipk:
                break
            print(f"  [Error] {err_ipk[0]}")
            
        # Validasi Input SKS
        while True:
            sks_str = input("Masukkan SKS (0-24)    : ").strip()
            val_sks, err_sks = validasi_data.validasi_sks(sks_str)
            if not err_sks:
                break
            print(f"  [Error] {err_sks[0]}")
            
        # Evaluasi Status
        status = status_mahasiswa.tentukan_status(val_ipk, val_sks)
        
        print("\n" + "-" * 50)
        print(f" HASIL EVALUASI STATUS AKADEMIK MAHASISWA")
        print("-" * 50)
        print(f" NIM       : {nim}")
        print(f" Nama      : {nama}")
        print(f" IPK       : {val_ipk:.2f}")
        print(f" SKS       : {val_sks}")
        print(f" STATUS    : {status.upper()}")
        print("-" * 50)
        
    elif pilihan == "2":
        print("\nMemuat laporan status 5 mahasiswa...")
        sample_data = status_mahasiswa.get_sample_data()
        status_mahasiswa.tampilkan_laporan(sample_data)
        
    elif pilihan == "0":
        return
    else:
        print("  [Error] Pilihan submenu tidak valid!")


def submenu_hitung_diskon():
    """Submenu (2): Hitung Diskon Biaya Kuliah."""
    print("\n" + "=" * 60)
    print(f"{'SUBMENU 2: KALKULATOR DISKON BIAYA KULIAH (SPP)':^60}")
    print("=" * 60)
    
    # Run interactive calculation from diskon_biaya module
    diskon_biaya.input_dan_hitung()


def submenu_cek_stok():
    """Submenu (3): Cek Peringatan Stok Inventaris."""
    print("\n" + "=" * 60)
    print(f"{'SUBMENU 3: SISTEM PERINGATAN STOK INVENTARIS':^60}")
    print("=" * 60)
    
    # Run stock evaluation from peringatan_stok module
    inventaris = peringatan_stok.get_default_inventaris()
    peringatan_stok.proses_laporan_stok(inventaris)


def main():
    """Menu Interaktif Utama menggunakan While Loop."""
    while True:
        print("\n" + "=" * 60)
        print(f"{'APLIKASI SISTEM INFORMASI MAHASISWA':^60}")
        print("=" * 60)
        print(" [1] Cek Status Mahasiswa")
        print(" [2] Hitung Diskon Biaya Kuliah")
        print(" [3] Cek Peringatan Stok Barang")
        print(" [0] Keluar Aplikasi")
        print("=" * 60)
        
        pilihan = input("Pilih Menu (0-3): ").strip()
        
        if pilihan == "1":
            submenu_cek_status_mahasiswa()
        elif pilihan == "2":
            submenu_hitung_diskon()
        elif pilihan == "3":
            submenu_cek_stok()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Sistem Informasi Mahasiswa.")
            print("Program selesai.")
            break
        else:
            print("\n  [Error] Pilihan menu tidak valid! Silakan masukkan angka 0, 1, 2, atau 3.")


if __name__ == "__main__":
    main()
