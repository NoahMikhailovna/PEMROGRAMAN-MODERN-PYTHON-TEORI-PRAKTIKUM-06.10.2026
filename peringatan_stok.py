"""
peringatan_stok.py
Sistem Peringatan Stok Inventaris Barang
==========================================
Modul Praktikum Pemrograman Python - Soal 3
"""

# Konstanta Aturan Bisnis Stok
BATAS_AMAN = 20
BATAS_PERINGATAN = 10


def eval_status_stok(stok: int):
    """
    Menevaluasi status, prioritas, dan rekomendasi berdasarkan jumlah stok:
    - Stok == 0     : Habis, Prioritas CRITICAL
    - 1 <= Stok <=10: Rendah, Prioritas HIGH
    - 11<= Stok <=20: Peringatan, Prioritas MEDIUM
    - Stok > 20     : Aman, Prioritas LOW
    """
    if stok == 0:
        return "Habis", "CRITICAL", "URGENT: Restock segera!"
    elif stok <= BATAS_PERINGATAN:
        return "Rendah", "HIGH", "Restock dalam 1-3 hari"
    elif stok <= BATAS_AMAN:
        return "Peringatan", "MEDIUM", "Rencanakan restock 1-2 minggu"
    else:
        return "Aman", "LOW", "Stok mencukupi"


def get_default_inventaris() -> list[dict]:
    """Mengembalikan data contoh inventaris barang (minimal 8 item)."""
    return [
        {"kode": "B001", "nama": "Buku Python", "stok": 45, "harga": 85000},
        {"kode": "B002", "nama": "Buku Database", "stok": 12, "harga": 95000},
        {"kode": "B003", "nama": "Flashdisk 16GB", "stok": 5, "harga": 50000},
        {"kode": "B004", "nama": "Kabel USB Type-C", "stok": 0, "harga": 25000},
        {"kode": "B005", "nama": "Mouse Wireless", "stok": 18, "harga": 120000},
        {"kode": "B006", "nama": "Keyboard Mech", "stok": 3, "harga": 350000},
        {"kode": "B007", "nama": "Monitor 24 Inch", "stok": 25, "harga": 1800000},
        {"kode": "B008", "nama": "HDD External 1TB", "stok": 0, "harga": 750000},
        {"kode": "B009", "nama": "Headset Gaming", "stok": 8, "harga": 200000},
    ]


def format_rupiah(nominal: float) -> str:
    """Format angka ke Rupiah (misal Rp 1.500.000)."""
    return f"Rp {nominal:,.0f}".replace(",", ".")


def proses_laporan_stok(inventaris: list[dict]):
    """Memproses evaluasi stok, menampilkan laporan, dan ringkasan statistik."""
    print("=" * 85)
    print(f"{'LAPORAN EVALUASI & PERINGATAN STOK INVENTARIS':^85}")
    print("=" * 85)
    print(f"{'KODE':<6} {'NAMA BARANG':<20} {'STOK':>6} {'STATUS':<12} {'PRIORITAS':<10} {'REKOMENDASI':<25}")
    print("-" * 85)

    total_nilai = 0
    count_status = {"Aman": 0, "Peringatan": 0, "Rendah": 0, "Habis": 0}
    item_perlu_tindakan = 0

    for item in inventaris:
        status, prioritas, rekomendasi = eval_status_stok(item["stok"])
        nilai_item = item["stok"] * item["harga"]
        total_nilai += nilai_item
        count_status[status] += 1

        if prioritas != "LOW":
            item_perlu_tindakan += 1

        print(f"{item['kode']:<6} {item['nama']:<20} {item['stok']:>6} {status:<12} {prioritas:<10} {rekomendasi:<25}")

    print("=" * 85)

    # Ringkasan Statistik
    total_item = len(inventaris)
    persen_restock = (item_perlu_tindakan / total_item) * 100 if total_item > 0 else 0.0

    print("\n" + "=" * 50)
    print(f"{'RINGKASAN STATISTIK INVENTARIS':^50}")
    print("=" * 50)
    print(f" Total Jenis Barang       : {total_item} item")
    print(f" Jumlah Stok Aman         : {count_status['Aman']} item")
    print(f" Jumlah Stok Peringatan   : {count_status['Peringatan']} item")
    print(f" Jumlah Stok Rendah       : {count_status['Rendah']} item")
    print(f" Jumlah Stok Habis        : {count_status['Habis']} item")
    print("-" * 50)
    print(f" Item Perlu Tindakan      : {item_perlu_tindakan} dari {total_item} item ({persen_restock:.1f}%)")
    print(f" Total Nilai Inventaris   : {format_rupiah(total_nilai)}")
    print("=" * 50)


def main():
    inventaris = get_default_inventaris()
    proses_laporan_stok(inventaris)


if __name__ == "__main__":
    main()
