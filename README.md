# 🚀 Aplikasi CRUD Django

<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

**Aplikasi CRUD modern dan lengkap yang dibangun dengan Django**

[Demo](#demo) • [Fitur](#fitur) • [Instalasi](#instalasi) • [Penggunaan](#penggunaan) • [Kontribusi](#kontribusi)

</div>

---

## 📋 Daftar Isi

- [Tentang](#tentang)
- [Fitur](#fitur)
- [Demo](#demo)
- [Teknologi](#teknologi)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [API Endpoints](#api-endpoints)
- [Screenshot](#screenshot)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

---

## 🎯 Tentang

Proyek ini adalah aplikasi CRUD (Create, Read, Update, Delete) yang komprehensif dibangun dengan framework Django. Aplikasi ini mendemonstrasikan operasi fundamental manajemen database melalui antarmuka web yang intuitif, menjadikannya sempurna untuk belajar Django atau sebagai titik awal untuk proyek yang lebih besar.

## ✨ Fitur

- ✅ **Create** - Tambah data baru dengan validasi form
- 📖 **Read** - Lihat semua data dalam daftar yang rapi dan ter-paginasi
- ✏️ **Update** - Edit data yang ada dengan form yang sudah terisi
- 🗑️ **Delete** - Hapus data dengan konfirmasi
- 🎨 **UI Responsif** - Antarmuka Bootstrap yang mobile-friendly
- 🔍 **Pencarian & Filter** - Cari data spesifik dengan cepat
- 🔐 **Autentikasi User** - Sistem login dan registrasi yang aman
- 📱 **RESTful API** - API endpoint yang clean untuk semua operasi
- ⚡ **Performa Cepat** - Query database yang teroptimasi

## 🎬 Demo

> Tambahkan GIF atau video demo Anda di sini

```bash
# Quick start demo
python manage.py runserver
# Kunjungi http://127.0.0.1:8000
```

## 🛠️ Teknologi

Proyek ini dibangun dengan:

- **Backend Framework:** Django 4.x
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Template Engine:** Django Templates
- **Form Handling:** Django Forms dengan proteksi CSRF
- **Autentikasi:** Django Auth System

## 📥 Instalasi

### Prasyarat

Sebelum memulai, pastikan Anda sudah menginstall:
- Python 3.8 atau lebih tinggi
- pip (Python package installer)
- Git

### Panduan Step-by-Step

1. **Clone repository**
   ```bash
   git clone https://github.com/Aksan-12/crud_Python_Django.git
   cd crud_Python_Django
   ```

2. **Buat virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan migrasi**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Buat superuser** (Opsional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Jalankan development server**
   ```bash
   python manage.py runserver
   ```

7. **Buka browser Anda**
   
   Kunjungi `http://127.0.0.1:8000`

## 🎮 Penggunaan

### Operasi Dasar

#### Membuat Data Baru
1. Klik tombol "Tambah Baru"
2. Isi field yang diperlukan
3. Klik "Submit" untuk menyimpan

#### Melihat Data
- Semua data ditampilkan di halaman utama
- Gunakan pagination untuk navigasi melalui beberapa halaman
- Klik data untuk melihat detail

#### Mengupdate Data
1. Klik tombol "Edit" pada data yang ingin diubah
2. Modifikasi field sesuai kebutuhan
3. Klik "Update" untuk menyimpan perubahan

#### Menghapus Data
1. Klik tombol "Delete" pada data yang ingin dihapus
2. Konfirmasi penghapusan di popup
3. Data akan dihapus secara permanen

### Panel Admin

Akses panel admin Django di `http://127.0.0.1:8000/admin` dengan kredensial superuser Anda untuk mengelola:
- User dan permissions
- Data database
- Pengaturan aplikasi

## 📁 Struktur Proyek

```
crud_Python_Django/
├── 📂 myapp/                  # Direktori aplikasi utama
│   ├── 📂 migrations/         # Migrasi database
│   ├── 📂 templates/          # Template HTML
│   │   └── 📂 myapp/
│   │       ├── index.html
│   │       ├── create.html
│   │       ├── update.html
│   │       └── detail.html
│   ├── 📂 static/             # File statis (CSS, JS, gambar)
│   ├── __init__.py
│   ├── admin.py               # Konfigurasi admin
│   ├── apps.py                # Konfigurasi aplikasi
│   ├── models.py              # Model database
│   ├── views.py               # Fungsi view
│   ├── urls.py                # Pola URL
│   └── forms.py               # Definisi form
├── 📂 project/                # Direktori pengaturan proyek
│   ├── __init__.py
│   ├── settings.py            # Pengaturan proyek
│   ├── urls.py                # Konfigurasi URL utama
│   └── wsgi.py                # Konfigurasi WSGI
├── 📄 manage.py               # Script manajemen Django
├── 📄 requirements.txt        # Dependensi proyek
├── 📄 .gitignore             # File git ignore
├── 📄 db.sqlite3             # Database SQLite
└── 📄 README.md              # File ini
```

## 🔌 API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Tampilkan semua data |
| GET | `/create/` | Tampilkan form tambah data |
| POST | `/create/` | Buat data baru |
| GET | `/update/<id>/` | Tampilkan form edit |
| POST | `/update/<id>/` | Update data |
| GET | `/delete/<id>/` | Hapus data |
| GET | `/detail/<id>/` | Lihat detail data |

## 📸 Screenshot

> Tambahkan screenshot aplikasi Anda di sini

### Halaman Utama
![Halaman Utama](link-to-screenshot)

### Form Tambah Data
![Form Tambah](link-to-screenshot)

### Form Edit Data
![Form Edit](link-to-screenshot)

## 🤝 Kontribusi

Kontribusi adalah apa yang membuat komunitas open source menjadi tempat yang luar biasa untuk belajar, menginspirasi, dan berkreasi. Setiap kontribusi yang Anda berikan **sangat dihargai**.

1. Fork Proyek ini
2. Buat Feature Branch (`git checkout -b feature/FiturBaru`)
3. Commit perubahan Anda (`git commit -m 'Menambahkan FiturBaru'`)
4. Push ke Branch (`git push origin feature/FiturBaru`)
5. Buka Pull Request

## 📝 Lisensi

Didistribusikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk informasi lebih lanjut.

## 📧 Kontak

**Aksan**

- GitHub: [@Aksan-12](https://github.com/Aksan-12)
- Link Proyek: [https://github.com/Aksan-12/crud_Python_Django](https://github.com/Aksan-12/crud_Python_Django)

---

