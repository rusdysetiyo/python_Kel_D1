import time


def disclaimer():
    print("\n" + "!" * 65)
    print(" [ PASAL SANGGAHAN / DISCLAIMER KEPATUHAN HUKUM ]")
    print("!" * 65)
    print("Program simulasi ini adalah murni KARYA FIKSI PARODI yang")
    print("dibuat semata-mata untuk keperluan akademis dan hiburan.")
    print("Segala kesamaan nama tokoh (termasuk Pangeran Soloman),")
    print("gelar, instansi, tempat, maupun peristiwa sejarah adalah")
    print("KEBETULAN BELAKA dan tidak merujuk pada individu, pejabat,")
    print("atau entitas nyata mana pun di dunia nyata.")
    print("-" * 65)
    # Fitur nunggu persetujuan pemain
    input(">> Tekan [ENTER] untuk menyetujui dan melanjutkan... ")
    print("[SISTEM] Persetujuan diterima. Membuka protokol utama...\n")
    time.sleep(1)

def opening():
    print("=" * 65)
    print(" ARSIP NEGARA: OPERASI TEMBOK RATAPAN SOLO")
    print("=" * 65)
    print("Tahun 202X. Akses menuju Ring 1 Istana telah diblokir sepenuhnya.")
    print("Penjagaan diambil alih oleh Pasukan Termul di bawah komando")
    print("Pangeran Soloman. Metode interogasi: Matematika Ekstrem.")
    print("Hanya pihak yang memiliki izin tingkat tinggi yang dapat melintas.")
    print("-" * 65)
    time.sleep(1.5)
    print("\n[SISTEM DUKCAPIL] Sinkronisasi basis data kependudukan...")
    print("[SISTEM DUKCAPIL] Menunggu otorisasi identitas...\n")

def game_over(nama):
    print("\n" + "-" * 65)
    print("[STATUS : ELIMINASI DINI]")
    print("PERINGATAN DARI OTORITAS TEMPLE OF SOLOMAN!")
    print("-" * 65)
    print(f"Elektabilitas Subjek [{nama}] telah menyentuh ambang batas bawah.")
    print("Tindakan makar secara matematis telah berhasil digagalkan.")
    print("Sanksi Administratif: Relokasi paksa ke kamp pekerja sawit kerajaan.")
    print("-" * 65)

def tamat(nama):
    print("\n" + "=" * 65)
    print("[STATUS : OTORISASI PENUH]")
    print("PENGAMBILALIHAN KEKUASAAN BERHASIL")
    print("=" * 65)
    print(f"Subjek [{nama}] telah menembus pertahanan lapis terakhir.")
    print("Rezim Pangeran Soloman secara resmi dinyatakan demisioner.")
    print("Akses ke Temple of Soloman dan seluruh aset kebun sawit negara")
    print("kini sepenuhnya berada di bawah kendali Anda.")
    print("=" * 65)