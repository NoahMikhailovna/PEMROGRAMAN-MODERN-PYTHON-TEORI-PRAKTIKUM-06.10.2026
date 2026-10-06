"""
ringkasan_algoritma.py
Ringkasan Metrik Algoritma dari Ketiga Studi Kasus
===================================================
Modul Praktikum Pemrograman Python - Soal 6
"""

import status_mahasiswa
import diskon_biaya
import peringatan_stok


def hitung_persentase_status_mahasiswa():
    """
    (a) Hitung persentase mahasiswa aktif vs tidak aktif (dan peringatan)
    dari sampel data mahasiswa.
    """
    daftar_mhs = status_mahasiswa.get_sample_data()
    total = len(daftar_mhs)
    
    count_aktif = 0
    count_peringatan = 0
    count_tidak_aktif = 0
    
    for mhs in daftar_mhs:
        st = status_mahasiswa.tentukan_status(mhs["ipk"], mhs["sks"])
        if st == "Aktif":
            count_aktif += 1
        elif st == "Peringatan":
            count_peringatan += 1
        elif st == "Tidak Aktif":
            count_tidak_aktif += 1
            
    pct_aktif = (count_aktif / total) * 100 if total > 0 else 0
    pct_peringatan = (count_peringatan / total) * 100 if total > 0 else 0
    pct_tidak_aktif = (count_tidak_aktif / total) * 100 if total > 0 else 0
    pct_non_aktif_total = ((count_peringatan + count_tidak_aktif) / total) * 100 if total > 0 else 0
    
    return {
        "total": total,
        "count_aktif": count_aktif,
        "count_peringatan": count_peringatan,
        "count_tidak_aktif": count_tidak_aktif,
        "pct_aktif": pct_aktif,
        "pct_peringatan": pct_peringatan,
        "pct_tidak_aktif": pct_tidak_aktif,
        "pct_non_aktif_total": pct_non_aktif_total
    }


def hitung_rata_rata_diskon():
    """
    (b) Hitung rata-rata diskon yang diberikan dari sampel beberapa skenario transaksi.
    """
    sample_transaksi = [
        {"nama": "Mahasiswa A", "ipk": 3.90, "anak_karyawan": False, "tepat_waktu": True},   # Diskon: 20% + 5% = 25%
        {"nama": "Mahasiswa B", "ipk": 3.55, "anak_karyawan": True,  "tepat_waktu": False},  # Diskon: 25% + 0% = 25%
        {"nama": "Mahasiswa C", "ipk": 2.80, "anak_karyawan": False, "tepat_waktu": True},   # Diskon: 0%  + 5% = 5%
        {"nama": "Mahasiswa D", "ipk": 3.20, "anak_karyawan": False, "tepat_waktu": False},  # Diskon: 10% + 0% = 10%
        {"nama": "Mahasiswa E", "ipk": 2.40, "anak_karyawan": False, "tepat_waktu": False},  # Diskon: 0%  + 0% = 0%
    ]
    
    total_diskon = 0.0
    detail_diskon = []
    
    for tx in sample_transaksi:
        total_d, _, _, _ = diskon_biaya.hitung_diskon(tx["ipk"], tx["anak_karyawan"], tx["tepat_waktu"])
        total_diskon += total_d
        detail_diskon.append({
            "nama": tx["nama"],
            "diskon": total_d
        })
        
    rata_rata_diskon = (total_diskon / len(sample_transaksi)) * 100 if sample_transaksi else 0.0
    
    return {
        "total_transaksi": len(sample_transaksi),
        "rata_rata_diskon_pct": rata_rata_diskon,
        "detail": detail_diskon
    }


def hitung_persentase_restock():
    """
    (c) Hitung persentase item yang perlu restock dari inventaris.
    (Stok <= 20 atau Status Habis/Rendah/Peringatan).
    """
    inventaris = peringatan_stok.get_default_inventaris()
    total_item = len(inventaris)
    count_restock = 0
    
    for item in inventaris:
        _, prioritas, _ = peringatan_stok.eval_status_stok(item["stok"])
        if prioritas != "LOW":  # Membutuhkan restock (CRITICAL, HIGH, MEDIUM)
            count_restock += 1
            
    pct_restock = (count_restock / total_item) * 100 if total_item > 0 else 0.0
    
    return {
        "total_item": total_item,
        "count_restock": count_restock,
        "pct_restock": pct_restock
    }


def tampilkan_ringkasan_tabel():
    res_mhs = hitung_persentase_status_mahasiswa()
    res_diskon = hitung_rata_rata_diskon()
    res_stok = hitung_persentase_restock()
    
    print("=" * 80)
    print(f"{'TABEL RINGKASAN ALGORITMA DARI 3 STUDI KASUS':^80}")
    print("=" * 80)
    print(f"{'NO':<4} {'INDIKATOR ALGORITMA':<35} {'DATA SAMPEL':<16} {'HASIL METRIK':<20}")
    print("-" * 80)
    
    # Section (a)
    print(f"{'1':<4} {'(a) Mahasiswa Aktif':<35} {res_mhs['total']:>2} Mahasiswa     {res_mhs['pct_aktif']:>6.2f}% ({res_mhs['count_aktif']}/{res_mhs['total']} Mhs)")
    print(f"{' ': <4} {'    Mahasiswa Peringatan':<35} {res_mhs['total']:>2} Mahasiswa     {res_mhs['pct_peringatan']:>6.2f}% ({res_mhs['count_peringatan']}/{res_mhs['total']} Mhs)")
    print(f"{' ': <4} {'    Mahasiswa Tidak Aktif':<35} {res_mhs['total']:>2} Mahasiswa     {res_mhs['pct_tidak_aktif']:>6.2f}% ({res_mhs['count_tidak_aktif']}/{res_mhs['total']} Mhs)")
    print(f"{' ': <4} {'    Total Non-Aktif (Peringatan+Tdk Aktif)':<35} {res_mhs['total']:>2} Mahasiswa     {res_mhs['pct_non_aktif_total']:>6.2f}% ({res_mhs['count_peringatan']+res_mhs['count_tidak_aktif']}/{res_mhs['total']} Mhs)")
    print("-" * 80)
    
    # Section (b)
    print(f"{'2':<4} {'(b) Rata-Rata Diskon SPP Diberikan':<35} {res_diskon['total_transaksi']:>2} Sampel Mhs     {res_diskon['rata_rata_diskon_pct']:>6.2f}%")
    print("-" * 80)
    
    # Section (c)
    print(f"{'3':<4} {'(c) Item Inventaris Perlu Restock':<35} {res_stok['total_item']:>2} Item Barang    {res_stok['pct_restock']:>6.2f}% ({res_stok['count_restock']}/{res_stok['total_item']} Item)")
    print("=" * 80)


def main():
    tampilkan_ringkasan_tabel()


if __name__ == "__main__":
    main()
