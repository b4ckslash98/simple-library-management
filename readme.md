## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan proyek ini:

1. **Install Python v3.7+**
   - Pastikan Python versi 3.7 atau lebih baru telah terinstal. Anda dapat mengunduhnya dari [situs resmi Python](https://www.python.org/downloads/).

2. **Buat Virtual Environment**
   - Disarankan untuk menggunakan virtual environment untuk mengelola dependensi proyek. Jalankan perintah berikut untuk membuat virtual environment:
     ```bash
     py -3.7 -m venv venv
     ```

3. **Aktifkan Virtual Environment**
   - Pada Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Pada macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependensi**
   - Setelah virtual environment diaktifkan, instal semua dependensi yang diperlukan dengan menjalankan:
     ```bash
     pip install -r requirements.txt
     ```

5. **Buat Migrasi Database**
   - Jalankan perintah berikut untuk membuat revisi migrasi awal menggunakan Alembic:
     ```bash
     alembic revision --autogenerate -m "init program"
     ```

6. **Terapkan Migrasi Database**
   - Terapkan migrasi dengan menjalankan:
     ```bash
     alembic upgrade head
     ```

7. **Jalankan Aplikasi**
   - Untuk menjalankan aplikasi, gunakan perintah:
     ```bash
     uvicorn app.main:app
     ```

## Pengujian

Jika Anda ingin menggunakan unit test, cukup jalankan perintah:
```bash
pytest
```