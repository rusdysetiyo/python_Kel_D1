import player
import stage_data
import battle
import tampilan
import evaluasi
import time


def bersihkan_layar():
    print("\033[H\033[J", end="")

def jalankan_game():
    tampilan.disclaimer()
    
    tampilan.opening()
    
    nama_pahlawan = input("Masukkan NIK / Identitas Rahasia Anda: ").strip()
    hero = player.buat_karakter(nama_pahlawan)
    
    print(f"\n[SISTEM] Verifikasi berhasil. Otorisasi sementara diberikan kepada [{hero['nama']}].")
    print("[SISTEM] Membuka gerbang utama menuju Ring 1...")
    time.sleep(2)
    
    level_sekarang = 1
    
    while True:
        stage_saat_ini = stage_data.get_stage(level_sekarang)
        
        if stage_saat_ini == None:
            tampilan.tamat(hero['nama'])
            evaluasi.cetak_raport(hero['nama'], hero['nyawa'], level_sekarang - 1, True)
            break

        print(f"\n" + "="*50)
        print(f"--- 🛑 MEMASUKI KAWASAN RING {level_sekarang} 🛑 ---")
        time.sleep(1)
        
        
        hasil_menang = battle.hadapi_monster(hero, stage_saat_ini)

        if hasil_menang == True:
            print("\n[SISTEM] Otorisasi Ring disetujui! Lanjut blusukan lebih dalam...")
            level_sekarang += 1
            time.sleep(1.5)
            
        else:
            tampilan.game_over(hero['nama'])
            evaluasi.cetak_raport(hero['nama'], hero['nyawa'], level_sekarang, False)
            break

if __name__ == "__main__":
    while True:
        jalankan_game()
        
        print("\n" + "="*65)
        print(" [SISTEM] Simulasi Operasi Tembok Ratapan Solo telah berakhir.")
        main_lagi = input(" >> Apakah Anda ingin mengajukan proposal infiltrasi ulang? (Y/N): ").upper()
        
        if main_lagi == 'Y':
            print("\n[SISTEM] Memproses ulang protokol infiltrasi...")
            time.sleep(1.5)
            
        else:
            print("\n[SISTEM] Menutup koneksi. Terima kasih atas partisipasi Anda.")
            time.sleep(1.5)
            bersihkan_layar()
            break