# Growtopia-Server-Status
Menampilkan Total Players Online, World of The Day, Growtopia Time/Date, Dengan Menggunakan Command Discord Bot. Live Demo: https://dsc.gg/fanking
Tentu, ini adalah contoh `README.md` yang menjelaskan cara menggunakan skrip Discord bot Anda, lengkap dengan contoh kode.


-----

# Growtopia Status Discord Bot

Bot Discord ini memungkinkan Anda untuk memeriksa status server Growtopia, termasuk jumlah pengguna online, World of the Day (WOTD), serta waktu dan tanggal Growtopia saat ini.

-----

## Fitur

  * Menampilkan jumlah **pengguna online** di Growtopia.
  * Menunjukkan **World of the Day (WOTD)** saat ini.
  * Menyediakan **waktu dan tanggal Growtopia** yang disinkronkan dengan zona waktu New York.
  * Menampilkan **gambar WOTD** sebagai thumbnail embed (jika tersedia).
  * Menangani kesalahan API dengan menampilkan data fallback.

-----

## Struktur Proyek

Proyek ini dipecah menjadi beberapa file Python untuk modularitas dan keterbacaan yang lebih baik:

```
your_project/
├── .env                  # Untuk menyimpan token Discord Anda
├── main.py               # Skrip utama yang menjalankan bot
├── growtopia_data.py     # Berisi fungsi untuk mengambil data Growtopia
└── bot_commands.py       # Berisi definisi perintah (commands) bot Discord
```

-----

## Persyaratan

Sebelum memulai, pastikan Anda memiliki hal-hal berikut:

  * **Python 3.8 atau lebih tinggi** terinstal di sistem Anda.
  * **Token Bot Discord** dari [Discord Developer Portal](https://discord.com/developers/applications).
  * Koneksi internet.

-----

## Instalasi

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan bot Anda:

1.  **Kloning repositori ini (atau buat file secara manual):**

    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd your_project
    ```

    Jika Anda membuat file secara manual, pastikan Anda memiliki struktur direktori seperti yang dijelaskan di bagian "Struktur Proyek".

2.  **Buat Lingkungan Virtual (Opsional, tetapi Disarankan):**

    ```bash
    python -m venv venv
    ```

      * Untuk Windows:
        ```bash
        .\venv\Scripts\activate
        ```
      * Untuk macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instal Dependensi:**

    ```bash
    pip install discord.py python-dotenv requests pytz
    ```

4.  **Konfigurasi File `.env`:**
    Buat file bernama `.env` di direktori root proyek Anda (setingkat dengan `main.py`). Masukkan token bot Discord Anda di dalamnya seperti ini:

    ```env
    DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
    ```

    **Ganti `YOUR_BOT_TOKEN_HERE`** dengan token bot Discord Anda yang sebenarnya.

-----

## Cara Menggunakan

1.  **Jalankan Bot:**
    Dari direktori root proyek Anda, jalankan skrip `main.py`:

    ```bash
    python main.py
    ```

    Anda akan melihat output di konsol yang menunjukkan bahwa bot telah online.

    ```
    Bot sudah online sebagai YourBotName#1234 (ID: 1234567890)
    ```

    Jika Anda melihat peringatan "⚠️ DISCORD\_TOKEN belum diatur di file .env", pastikan Anda telah mengonfigurasi file `.env` dengan benar.

2.  **Perintah Discord:**
    Setelah bot online dan terhubung ke server Discord Anda, Anda dapat menggunakan perintah berikut di saluran teks mana pun yang dapat diakses oleh bot:

      * `!status`: Menampilkan informasi status server Growtopia, termasuk pengguna online, WOTD, waktu, dan tanggal.

-----

## Contoh Penggunaan

Berikut adalah contoh bagaimana Anda dapat menggunakan perintah `!status` di Discord:

```
User: !status
```

Bot akan merespons dengan embed yang mirip dengan ini:

```
🌐 Growtopia Server Status
[Thumbnail gambar WOTD jika tersedia]

👥 Online User: 50000
🏷️ World of the Day: EXAMPLEWORLD
⏰ GT TIME: 07:00:00 PM
📅 GT DATE: July 01, 2025

FanKing Bot
```
