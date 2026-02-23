def buat_karakter(nama_input):
    # Ngembaliin nama n nyawa awal
    return {"nama": nama_input, "nyawa": 5}

def kurangi_nyawa(player_data):
    # Ngurang 1
    player_data["nyawa"] -= 1
    print(f"❌ Jawabanmu salah! Sisa nyawa: {player_data['nyawa']}")

def cek_mati(player_data):
    # Ngecek nyawa habis
    if player_data["nyawa"] <= 0:
        return True  # Mati
    else:
        return False # Masih hidup
