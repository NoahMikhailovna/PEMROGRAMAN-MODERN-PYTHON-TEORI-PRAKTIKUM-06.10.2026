"""
validasi_data.py
Fungsi Validasi Data Mahasiswa & Aturan Bisnis
===============================================
Modul Praktikum Pemrograman Python - Soal 5
"""

def validasi_nim(nim: str) -> list[str]:
    """
    Validasi NIM:
    - Harus 10 digit angka
    - Tahun masuk (4 digit pertama) harus antara 2000 dan 2037
    """
    errors = []
    nim_str = str(nim).strip()
    
    if not nim_str.isdigit():
        errors.append("NIM harus berupa 10 digit angka saja.")
    elif len(nim_str) != 10:
        errors.append(f"NIM harus persis 10 digit (panjang input: {len(nim_str)}).")
    else:
        tahun = int(nim_str[:4])
        if tahun < 2000 or tahun > 2037:
            errors.append(f"Tahun masuk pada NIM ({tahun}) harus antara tahun 2000 hingga 2037.")
            
    return errors


def validasi_ipk(ipk_val) -> tuple[float | None, list[str]]:
    """
    Validasi IPK:
    - Angka desimal di antara 0.0 dan 4.0
    """
    errors = []
    val_float = None
    try:
        val_float = float(ipk_val)
        if val_float < 0.0 or val_float > 4.0:
            errors.append(f"IPK ({val_float:.2f}) harus di dalam rentang 0.00 hingga 4.00.")
    except (ValueError, TypeError):
        errors.append("IPK harus berupa nilai numerik (angka desimal).")
        
    return val_float, errors


def validasi_sks(sks_val) -> tuple[int | None, list[str]]:
    """
    Validasi SKS:
    - Angka bulat di antara 0 dan 24
    """
    errors = []
    val_int = None
    try:
        val_int = int(sks_val)
        if val_int < 0 or val_int > 24:
            errors.append(f"Jumlah SKS ({val_int}) harus di dalam rentang 0 hingga 24.")
    except (ValueError, TypeError):
        errors.append("Jumlah SKS harus berupa angka bulat.")
        
    return val_int, errors


def validasi_semester(semester_val) -> tuple[int | None, list[str]]:
    """
    Validasi Semester:
    - Angka bulat di antara 1 dan 14
    """
    errors = []
    val_int = None
    try:
        val_int = int(semester_val)
        if val_int < 1 or val_int > 14:
            errors.append(f"Semester ({val_int}) harus di dalam rentang 1 hingga 14.")
    except (ValueError, TypeError):
        errors.append("Semester harus berupa angka bulat.")
        
    return val_int, errors


def validasi_data_mahasiswa(nim, ipk, sks, semester) -> list[str]:
    """
    Fungsi utama validasi data mahasiswa komposit.
    Mengembalikan list error jika terdapat data tidak valid.
    Jika semua valid, mengembalikan list kosong [].
    """
    all_errors = []
    
    # 1. Validasi NIM
    err_nim = validasi_nim(nim)
    all_errors.extend(err_nim)
    
    # 2. Validasi IPK
    _, err_ipk = validasi_ipk(ipk)
    all_errors.extend(err_ipk)
    
    # 3. Validasi SKS
    _, err_sks = validasi_sks(sks)
    all_errors.extend(err_sks)
    
    # 4. Validasi Semester
    _, err_sem = validasi_semester(semester)
    all_errors.extend(err_sem)
    
    return all_errors


def main():
    print("=" * 60)
    print(f"{'FORM VALIDASI DATA MAHASISWA':^60}")
    print("=" * 60)
    
    nim_input = input("Masukkan NIM (10 digit, thn 2000-2037): ").strip()
    ipk_input = input("Masukkan IPK (0.0 - 4.0)               : ").strip()
    sks_input = input("Masukkan SKS (0 - 24)                  : ").strip()
    semester_input = input("Masukkan Semester (1 - 14)             : ").strip()
    
    # Jalankan validasi
    errors = validasi_data_mahasiswa(nim_input, ipk_input, sks_input, semester_input)
    
    print("\n" + "=" * 60)
    print(f"{'HASIL EVALUASI VALIDASI':^60}")
    print("=" * 60)
    
    if not errors:
        print("[SUCCESS] HASIL: DATA MAHASISWA VALID!")
        print(f"  - NIM      : {nim_input}")
        print(f"  - IPK      : {float(ipk_input):.2f}")
        print(f"  - SKS      : {int(sks_input)}")
        print(f"  - Semester : {int(semester_input)}")
    else:
        print(f"[FAILED] Ditemukan {len(errors)} kesalahan data tidak valid:")
        for idx, err in enumerate(errors, start=1):
            print(f"  {idx}. {err}")
            
    print("=" * 60)


if __name__ == "__main__":
    main()
