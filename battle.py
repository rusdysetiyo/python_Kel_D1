import player 

def hadapi_monster(player_data, stage_data):
    print("\n" + "="*40)
    print(f"⚠️ Tiba-tiba muncul {stage_data['nama_monster']}!")
    print(stage_data['narasi'])
    print("-" * 40)
    print(stage_data['pertanyaan'])
    print(stage_data['pilihan'])

    # Looping sampai jawaban benar atau pemain mati
    while True:
        # Meminta input dan otomatis diubah jadi huruf besar (A/B/C)
        jawaban_user = input("Jawabanmu (A/B/C): ").upper()
        if jawaban_user not in ["A", "B", "C"]:
                print("⚠️ Pilihan tidak valid! Masukkan hanya A, B, atau C.")
                continue
        if jawaban_user == stage_data['jawaban_benar']:
            print("✅ BENAR! Monster itu berhasil dikalahkan!")
            return True 
        else:
            player.kurangi_nyawa(player_data) 
            if player.cek_kematian(player_data) == True:
                return False 
            else:
                print("Coba tebak lagi!")
