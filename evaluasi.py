def hitung_skor(nyawa_sisa, level_terakhir):
    skor_level = level_terakhir * 20
    bonus_nyawa = nyawa_sisa * 15
    total_skor = skor_level + bonus_nyawa
    return total_skor

def cetak_raport(nama, nyawa_sisa, level_terakhir, menang_tamat):
    skor = hitung_skor(nyawa_sisa, level_terakhir)
    
    print("\n" + "="*65)
    print(" DOKUMEN RESMI NEGARA - RAHASIA TINGKAT I")
    print(" HASIL EVALUASI KINERJA APARATUR JALUR KHUSUS")
    print("="*65)
    print(f"Nama Pejabat Terafiliasi  : {nama}")
    print(f"Batas Penetrasi Ring      : Ring {level_terakhir}")
    print(f"Sisa Kuota Elektabilitas  : {nyawa_sisa}")
    print(f"Akumulasi Poin Pengaruh   : {skor} Poin")
    print("-" * 65)
    
    print("KEPUTUSAN PENEMPATAN JABATAN AKHIR:")
    if menang_tamat == True and nyawa_sisa >= 4:
        print("[SK-01] ELIT GLOBAL: Pemilik Saham Utama Konsorsium Sawit Soloman.")
    elif menang_tamat == True:
        print("[SK-02] MENTERI UTAMA: Tangan Kanan Pangeran (Jalur Khusus/Orang Dalam).")
    elif level_terakhir >= 4:
        print("[SK-03] KOMISARIS BUMN: Posisi aman, fasilitas negara terjamin.")
    elif level_terakhir >= 2:
        print("[SK-04] STAF AHLI MAGANG: Ditugaskan menyeduh kopi untuk Kapten B.Arie.")
    else:
        print("[SK-99] RAKYAT JELATA: Dicabut hak politiknya, dikirim ke kamp pekerja sawit.")
    print("="*65 + "\n")