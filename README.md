Link Domain : https://adjie-m-footballshop.pbp.cs.ui.ac.id/
Link Repo Github : https://github.com/adjiesidjaa/football-shop

Jawaban Pertanyaan Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Menginisialisasi projek & environment yang dibutuhkan
2. Mendefinisikan model Product di models.py
3. Mengatur file views.py
4. Mengatur file urls.py
5. Membuat template folder template
6. Membuat file main dan product_list
7. Coding dan mengimport cdn tailwind agar bisa mengatur tampilannya
8. Melihat tampilan website dengan run local
9. Mendeploy ke pws dan push ke github
10. Membuat README.md

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
ada di file bagan penjelasan req client.png


3. Jelaskan peran settings.py dalam proyek Django!
settings.py itu pusat kendali satu projek di django. Semua konfigurasi inti yang nyambung ke semua hal di projek ditaruh di situ untuk jadi tempat buat ngatur semuanya. Singkatnya, settings.py itu blueprint environment yang membuat aplikasi dapat berjalan sesuai mode (dev dan production) tanpa perlu mengubah kode logika di app.

4. Bagaimana cara kerja migrasi database di Django?
Pertama, kita buat/mengubah model yang sudah ada
Kedua, kita menjalankan makemigrations yang membuat django membuat file migrasi otomatis
Ketiga, menjalankan migrate. File migrasi yang telah dibuat tadi dieksekusi, membuat tabel baru atau update kolom yang berubah.
Semua langkah ini dicatat oleh django historinya, jadi urutannya terlihat jelas dan dapat di-rollback kalau dibutuhkan.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Saya rasa, alasan Django dijadikan sebagai permulaan pembelajaran karena kita telah mempelajari python terlebih dahulu sebelumnya. Selain itu, django sudah cukup lengkap buat pemula yang belum mengerti mengenai pengembangan perangkat lunak. Django juga tidak terlalu ribet untuk setupnya, tetapi tetap memiliki fitur yang banyak.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Untuk sekarang, belum ada.

Jawaban Pertanyaan Tugas 3
1. Mengapa Kita Memerlukan Data Delivery dalam Platform?

Data delivery penting supaya platform bisa bertukar data antar bagian sistem dengan rapi. Platform biasanya punya banyak komponen: frontend, backend, database, bahkan bisa diakses oleh aplikasi mobile atau layanan pihak ketiga. Jadi, kita perlu mekanisme untuk mengirimkan data dalam format yang konsisten supaya bisa dibaca semua bagian sistem tanpa masalah.
Kalau data hanya ditampilkan dalam HTML saja, kita tidak bisa dengan mudah mengakses datanya dari aplikasi lain. Dengan adanya data delivery seperti JSON atau XML, platform kita jadi bisa dipakai untuk API, integrasi dengan aplikasi lain, dan memudahkan pengembangan fitur di masa depan.

2. XML vs JSON, dan Kenapa JSON Lebih Populer

Secara teknis, JSON dan XML sama-sama bisa dipakai untuk menyimpan dan mengirimkan data. Tapi JSON biasanya lebih ringkas dan mudah dibaca manusia. JSON juga lebih cocok untuk aplikasi web modern karena bisa langsung diproses oleh JavaScript tanpa parsing yang ribet.
XML cenderung lebih verbose (pakai banyak tag pembuka-penutup) dan lebih cocok kalau kita perlu struktur data yang kompleks atau validasi schema yang ketat.
Karena aplikasi web sekarang butuh kecepatan dan efisiensi, JSON lebih sering dipakai dibanding XML.

3. Fungsi is_valid() pada Form Django

Method is_valid() digunakan untuk memvalidasi data yang dikirim dari form. Kalau is_valid() mengembalikan True, artinya semua data yang dikirim sudah sesuai aturan yang kita tetapkan di form dan model (misalnya tidak kosong, format email benar, harga berupa angka, dll).
Kita butuh method ini supaya data yang masuk ke database selalu bersih dan sesuai format. Kalau kita langsung simpan tanpa validasi, bisa ada data yang salah format atau bahkan berbahaya masuk ke sistem.

4. Fungsi csrf_token pada Form Django

csrf_token adalah token keamanan yang digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery). Serangan ini memanfaatkan celah di mana penyerang membuat user tanpa sadar mengirimkan request berbahaya (misalnya submit form untuk menghapus data) ke server saat user sedang login.
Kalau kita tidak menambahkan csrf_token, penyerang bisa memanfaatkan celah itu untuk menjalankan aksi tanpa izin. Dengan token ini, setiap form hanya bisa diproses kalau request-nya membawa token yang valid, sehingga lebih aman.

5. Step-by-Step Implementasi Checklist

Membuat base.html sebagai kerangka template utama supaya tampilan konsisten di semua halaman.

Membuat model Product di models.py untuk menyimpan data produk.

Membuat views: product_list, create_product, dan product_detail untuk menampilkan list produk, membuat produk baru, dan menampilkan detail produk.

Membuat forms.py yang berisi ProductForm berbasis ModelForm supaya form otomatis sesuai dengan model.

Membuat template untuk setiap halaman (product_list.html, create_product.html, product_detail.html) dan extend base.html.

Menambahkan routing di urls.py supaya setiap halaman bisa diakses dengan URL yang jelas.

Menambahkan views untuk data delivery (product_json, product_xml, product_json_by_id, product_xml_by_id) supaya data produk bisa diakses dalam format JSON dan XML.

Menjalankan server dan testing di Postman untuk memastikan data keluar sesuai format yang diinginkan.

Commit & push ke GitHub supaya hasilnya tersimpan dan bisa dideploy ke PWS.

6. Feedback untuk Asdos

Menurut saya, tutorial ini sudah cukup jelas dan runtut. Bagian penjelasan tentang serializers dan perbedaan JSON/XML sudah membantu memahami konsep data delivery. Akan lebih baik kalau disediakan contoh error yang umum muncul (misalnya NoReverseMatch atau ValidationError) beserta solusinya supaya mahasiswa bisa cepat troubleshooting saat praktikum.

Foto postman berada di folder foto readme
