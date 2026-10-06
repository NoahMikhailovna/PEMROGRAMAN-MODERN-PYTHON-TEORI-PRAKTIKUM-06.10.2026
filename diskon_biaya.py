"""
diskon_biaya.py
Kalkulator Diskon Biaya Kuliah (SPP)
=====================================
Modul Praktikum Pemrograman Python - Soal 2
"""

# Konstanta Aturan Bisnis Diskon
DISKON_ANAK_KARYAWAN = 0.25
DISKON_IPK_38 = 0.20
DISKON_IPK_35 = 0.15
DISKON_IPK_30 = 0.10
DISKON_TEPAT_WAKTU = 0.05


def hitung_diskon(ipk: float, is_anak_karyawan: bool, is_tepat_waktu: bool):
    """
    Menhitung persentase diskon berdasarkan aturan bisnis:
    1. Diskon Utama (ambil yang terbesar / tidak kumulatif):
       - Anak Karyawan : 25%
       - IPK >= 3.8    : 20%
       - IPK >= 3.5    : 15%
       - IPK >= 3.0    : 10%
    2. Diskon Tambahan:
       - Tepat waktu   : +5% (selalu ditambahkan jika True)

    Returns:
        tuple: (total_diskon, diskon_utama, diskon_tambahan, kategori_utama)
    """
    if is_anak_karyawan:
        diskon_utama = DISKON_ANAK_KARYAWAN
        kategori_utama = "Anak Karyawan (25%)"
    elif ipk >= 3.8:
        diskon_utama = DISKON_IPK_38
        kategori_utama = "Prestasi Tinggi - IPK >= 3.8 (20%)"
    elif ipk >= 3.5:
        diskon_utama = DISKON_IPK_35
        kategori_utama = "Prestasi Baik - IPK >= 3.5 (15%)"
    elif ipk >= 3.0:
        diskon_utama = DISKON_IPK_30
        kategori_utama = "Prestasi Memuaskan - IPK >= 3.0 (10%)"
    else:
        diskon_utama = 0.0
        kategori_utama = "Tidak Ada Diskon Utama (0%)"

    diskon_tambahan = DISKON_TEPAT_WAKTU if is_tepat_waktu else 0.0
    total_diskon = diskon_utama + diskon_tambahan

    return total_diskon, diskon_utama, diskon_tambahan, kategori_utama


def format_rupiah(nominal: float) -> str:
    """Format angka ke format mata uang Rupiah (contoh: Rp 5.000.000)."""
    return f"Rp {nominal:,.0f}".replace(",", ".")


def input_dan_hitung():
    print("=" * 60)
    print(f"{'KALKULATOR DISKON BIAYA KULIAH (SPP)':^60}")
    print("=" * 60)

    # Input Biaya SPP
    while True:
        try:
            biaya_spp = float(input("Masukkan Biaya SPP Dasar (Rp)  : "))
            if biaya_spp >= 0:
                break
            print("  [Error] Biaya SPP tidak boleh negatif!")
        except ValueError:
            print("  [Error] Masukkan nominal angka yang valid!")

    # Input Status Anak Karyawan
    is_anak_karyawan = input("Apakah Anak Karyawan? (y/n)      : ").strip().lower() == 'y'

    # Input IPK
    while True:
        try:
            ipk = float(input("Masukkan IPK (0.00 - 4.00)       : "))
            if 0.0 <= ipk <= 4.0:
                break
            print("  [Error] IPK harus di antara 0.00 dan 4.00!")
        except ValueError:
            print("  [Error] Masukkan angka IPK yang valid!")

    # Input Status Tepat Waktu
    is_tepat_waktu = input("Bayar Tepat Waktu? (y/n)         : ").strip().lower() == 'y'

    # Kalkulasi
    total_d, d_utama, d_tambahan, kat_utama = hitung_diskon(ipk, is_anak_karyawan, is_tepat_waktu)
    potongan_biaya = biaya_spp * total_d
    biaya_final = biaya_spp - potongan_biaya

    # Output Laporan
    print("\n" + "=" * 60)
    print(f"{'RINCIAN PERHITUNGAN BIAYA KULIAH':^60}")
    print("=" * 60)
    print(f"Biaya SPP Awal          : {format_rupiah(biaya_spp)}")
    print(f"Status Anak Karyawan    : {'Ya' if is_anak_karyawan else 'Tidak'}")
    print(f"IPK Mahasiswa           : {ipk:.2f}")
    print(f"Pembayaran Tepat Waktu  : {'Ya (+5%)' if is_tepat_waktu else 'Tidak (0%)'}")
    print("-" * 60)
    print(f"Kategori Diskon Utama   : {kat_utama}")
    print(f"Diskon Utama            : {d_utama * 100:.0f}%")
    print(f"Diskon Tambahan         : {d_tambahan * 100:.0f}%")
    print(f"Total Diskon Berlaku    : {total_d * 100:.0f}%")
    print("-" * 60)
    print(f"Potongan Biaya (Diskon) : {format_rupiah(potongan_biaya)}")
    print(f"BIAYA FINAL (BAYAR)     : {format_rupiah(biaya_final)}")
    print("=" * 60)

    return {
        "biaya_spp": biaya_spp,
        "is_anak_karyawan": is_anak_karyawan,
        "ipk": ipk,
        "is_tepat_waktu": is_tepat_waktu,
        "total_diskon": total_d,
        "potongan_biaya": potongan_biaya,
        "biaya_final": biaya_final
    }


if __name__ == "__main__":
    input_dan_hitung()
