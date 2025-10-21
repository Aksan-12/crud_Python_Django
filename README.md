Aplikasi CRUD Data Mahasiswa (Python & Flask)
Ini adalah proyek aplikasi web sederhana yang mengimplementasikan fungsionalitas CRUD (Create, Read, Update, Delete) untuk mengelola data mahasiswa. Aplikasi ini dibangun menggunakan Python dengan framework Flask dan menggunakan SQLite sebagai databasenya.

Aplikasi ini ditujukan untuk mendemonstrasikan dasar-dasar operasi database dalam aplikasi web menggunakan Flask-SQLAlchemy.

✨ Fitur Utama
Create: Menambahkan data mahasiswa baru (NIM, Nama, Prodi, Semester) ke dalam database melalui form.

Read: Menampilkan seluruh daftar mahasiswa yang tersimpan dalam tabel yang rapi di halaman utama.

Update: Mengedit dan memperbarui data mahasiswa yang sudah ada.

Delete: Menghapus data mahasiswa dari database dengan konfirmasi.

🛠️ Teknologi yang Digunakan
Backend: Python

Framework: Flask

Database: SQLite

ORM: Flask-SQLAlchemy

Frontend: HTML, CSS (dengan template Jinja)

📸 Tampilan Aplikasi
1. Halaman Utama (Daftar Mahasiswa) Menampilkan semua data mahasiswa dalam tabel. Terdapat tombol untuk "Tambah", "Edit", dan "Hapus".

2. Halaman Tambah Mahasiswa Formulir untuk memasukkan data mahasiswa baru.

3. Halaman Edit Mahasiswa Formulir yang sudah terisi data sebelumnya untuk diedit.

🚀 Instalasi dan Cara Menjalankan
Berikut adalah langkah-langkah untuk menjalankan proyek ini di komputer lokal Anda.

Clone repositori ini:

Bash

git clone [URL-REPOSITORI-ANDA]
cd [NAMA-FOLDER-PROYEK]
(Disarankan) Buat dan aktifkan virtual environment:

Bash

# Untuk macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Untuk Windows
python -m venv venv
venv\Scripts\activate
Install dependensi yang diperlukan: Proyek ini memerlukan Flask dan Flask-SQLAlchemy.

Bash

pip install Flask Flask-SQLAlchemy
Jalankan aplikasi: File utama untuk aplikasi ini adalah App.py.

Bash

python App.py
Buka di browser: Setelah aplikasi berjalan, buka browser Anda dan kunjungi:

http://127.0.0.1:5000/
📁 Struktur File
.
├── App.py               # File utama aplikasi Flask (logika backend)
├── instance/
│   └── mahasiswa.db     # File database SQLite
├── screenshots/
│   ├── halaman-utama.png
│   ├── halaman-tambah.png
│   └── halaman-edit.png
├── templates/
│   ├── index.html       # Halaman utama (Read)
│   ├── tambah.html      # Halaman tambah data (Create)
│   └── edit.html        # Halaman edit data (Update)
└── README.md            # File ini
