# 🚀 Mini Web Server Keren dengan Python! 🌐

![Mini Web Server](/static/images.png)

Sebuah web server HTTP/1.1 sederhana yang dibangun dari dasar (_from scratch_) menggunakan Python, dengan fokus pada pemahaman fundamental protokol jaringan dan _socket programming_. Proyek ini dirancang sebagai studi kasus untuk mempelajari cara kerja web server dalam menangani koneksi TCP dan me-render halaman web statis.

> Proyek ini merupakan pengembangan mandiri yang diadaptasi dari tugas besar mata kuliah Jaringan Komputer.

## Abstrak Proyek

Di era _framework_ modern seperti Django dan Flask, sering kali kita melupakan apa yang sebenarnya terjadi di balik layar. Proyek ini adalah sebuah perjalanan kembali ke dasar: membangun sebuah server fungsional yang hanya berbekal modul standar Python, yaitu `socket` dan `threading`.

Tujuannya adalah untuk mendemonstrasikan dan memahami secara mendalam konsep-konsep inti dalam jaringan komputer, mulai dari pembuatan _socket_ TCP, siklus _request-response_ HTTP, hingga penanganan klien secara simultan.

## Konsep Inti & Tujuan Pembelajaran

Proyek ini secara praktis mengimplementasikan beberapa konsep fundamental jaringan komputer:

* **Socket Programming:** Membuka, mengikat (_bind_), mendengarkan (_listen_), dan menerima (_accept_) koneksi pada level TCP menggunakan modul `socket`.
* **Protokol HTTP/1.1:** Mem-parsing request `GET` dari klien (seperti browser) dan membangun `response` HTTP yang valid (Status-Line, Headers, Body) sesuai standar.
* **Multithreading:** Menggunakan modul `threading` untuk mengelola beberapa koneksi klien secara bersamaan, mencegah server berhenti melayani saat menangani satu permintaan yang lama.
* **Arsitektur Perangkat Lunak Modular:** Merancang server dengan struktur yang bersih dan terpisah antara logika inti (parsing, response building), _request handlers_, dan konfigurasi.
* **MIME Types:** Mengenali tipe file yang diminta (HTML, CSS, PNG, dll.) dan menyertakan header `Content-Type` yang benar agar browser dapat me-render-nya dengan tepat.

## Fitur Utama

* **Penanganan Koneksi Multithreaded:** Mampu melayani banyak klien secara simultan tanpa _blocking_.
* **Parsing HTTP GET Request:** Mengekstrak metode, _path_, dan versi HTTP dari _raw request_.
* **Penyajian File Statis:** Menyajikan file HTML, CSS, JavaScript, dan gambar dari direktori `static/`.
* **Penanganan Error:** Mengirimkan response `404 Not Found` jika file tidak ada dan `500 Internal Server Error` jika terjadi kesalahan di sisi server.
* **Logging Profesional:** Mencatat aktivitas server (koneksi masuk, _request_, dan error) dengan format yang jelas untuk kemudahan _debugging_.
* **Struktur Proyek Skalabel:** Kode diorganisir ke dalam modul-modul yang memiliki tanggung jawab tunggal.

## Struktur Proyek

```
MiniWebServer/
├── static/
│   ├── index.html
│   └── style.css
├── server/
│   ├── core/
│   │   ├── request.py      # Kelas untuk parsing request
│   │   └── response.py     # Kelas untuk membangun response
│   ├── handlers/
│   │   └── static_handler.py # Logika untuk menyajikan file statis
│   ├── utils/
│   │   └── logger.py       # Konfigurasi logging
│   └── main.py             # Kelas Server utama dan loop koneksi
├── config.py               # Konfigurasi HOST dan PORT
├── run_server.py           # Titik masuk untuk menjalankan server
└── README.md
```

## Cara Menjalankan

Proyek ini tidak memerlukan dependensi eksternal, hanya Python 3.

1. **Clone Repositori**
   
   ```bash
   git clone https://github.com/RozhakXD/MiniWebServer.git
   cd MiniWebServer
   ```
2. **Jalankan Server**
    Buka terminal di direktori utama proyek dan jalankan perintah:
   
   ```bash
   python run_server.py
   ```
   
    Server akan berjalan dan menampilkan log di terminal:
   
   ```text
   2025-07-08 18:51:29 - INFO - Server akan berjalan di 127.0.0.1:6789
   2025-07-08 18:51:30 - INFO - Server berhasil berjalan, menunggu koneksi...
   ```
3. **Uji Coba**
    Buka browser favorit Anda dan kunjungi alamat berikut:
   * Halaman Utama: `http://127.0.0.1:6789`
   * Halaman Tidak Ditemukan: `http://127.0.0.1:6789/halaman-yang-tidak-ada`

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](/LICENSE).