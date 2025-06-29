# growtopia_data.py
import requests
from datetime import datetime
from pytz import timezone
from urllib.parse import unquote

def get_growtopia_data():
    """
    Mengambil data Growtopia (jumlah pengguna online, WOTD, waktu & tanggal GT).
    Mengembalikan dictionary dengan data yang relevan.
    Menangani error jika API tidak dapat dijangkau.
    """
    result = {
        "Online_User": "N/A",
        "WOTDLink": "",
        "WOTDName": "",
        "GTTime": "",
        "GTDate": ""
    }
    try:
        # Coba ambil JSON dari endpoint official
        website = requests.get("https://www.growtopiagame.com/detail").json()

        result["Online_User"] = website.get("online_user", "N/A")
        result["WOTDLink"] = website.get("world_day_images", {}).get("full_size", "") or ""

        # Jika JSON memberikan link yang valid (diawali http/https), parse langsung
        if result["WOTDLink"].startswith("http://") or result["WOTDLink"].startswith("https://"):
            # Ambil nama file terakhir, unquote, hapus ".png", lalu uppercase
            filename = unquote(result["WOTDLink"].split("/")[-1])
            result["WOTDName"] = filename.replace(".png", "").upper()
        else:
            # Jika link kosong atau tidak valid, gunakan URL fallback
            fallback_url = "https://www.growtopiagame.com/worlds/infernalcitadel.png"
            filename = unquote(fallback_url.split("/")[-1])
            result["WOTDName"] = filename.replace(".png", "").upper()
            result["WOTDLink"] = "" # Biarkan WOTDLink tetap kosong agar embed tidak memunculkan thumbnail/link

        # Waktu & tanggal di zona New York
        now_ny = datetime.now(timezone("UTC")).astimezone(timezone("America/New_York"))
        result["GTTime"] = now_ny.strftime("%I:%M:%S %p")  # Contoh: 07:45:12 PM
        result["GTDate"] = now_ny.strftime("%B %d, %Y")    # Contoh: June 01, 2025

    except Exception:
        # Jika terjadi exception (misalnya API down), gunakan fallback
        result["Online_User"] = "N/A"
        fallback_url = "https://www.growtopiagame.com/worlds/infernalcitadel.png"
        filename = unquote(fallback_url.split("/")[-1])
        result["WOTDName"] = filename.replace(".png", "").upper()
        result["WOTDLink"] = ""  # kosong, karena kita hanya ingin menampilkan nama world saja

        now_ny = datetime.now(timezone("UTC")).astimezone(timezone("America/New_York"))
        result["GTTime"] = now_ny.strftime("%I:%M:%S %p")
        result["GTDate"] = now_ny.strftime("%B %d, %Y")
    
    return result
