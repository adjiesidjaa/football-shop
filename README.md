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

Jawaban pertanyaan Tugas 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form bawaan Django untuk proses login. Form ini memvalidasi pasangan username–password terhadap backend autentikasi Django.
Kelebihan
-Siap pakai & aman: sudah menangani validasi kredensial, user aktif/nonaktif, dan error message standar.
-Terintegrasi ekosistem Django: cocok dengan authenticate(), login(), session, middleware, dan messages.
-Error message i18n: pesan error terjemahan tersedia.
Kekurangan
-Terbatas field: out-of-the-box hanya username & password (tanpa remember-me, 2FA, dsb).
-Styling minimal: butuh dibalut template/CSS sendiri agar tampil modern.
-Kustom validasi ekstra: untuk aturan khusus (mis. rate-limit per IP) perlu subclass/override.

2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah verifikasi siapa pengguna (login) sedangkan Otorisasi adalah verifikasi apa yang boleh dilakukan pengguna (hak akses). Autentikasi memverifikasi identitas pengguna menggunakan authenticate() dan login(). Jika berhasil, Django membuat session dan mengirim cookie sessionid ke browser. Middleware bawaan (AuthenticationMiddleware) kemudian menambahkan request.user ke setiap request sehingga aplikasi dapat mengenali pengguna yang sedang login. Otorisasi dilakukan setelah pengguna terautentikasi. Django memiliki sistem permission bawaan (add, change, delete, view) dan mendukung penambahan permission khusus. Pemeriksaan hak akses dapat dilakukan dengan user.has_perm() atau dekorator seperti @permission_required. Jika tidak memenuhi izin, pengguna akan diarahkan ke halaman login atau ditolak (403 Forbidden).

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan :
- lebih aman
- ukuran bebas (server side)
- ringan di server
- mudah diakses di klien
Kekurangan : 
- beban server/storage
- membutuhkan strategi shared cache/db untuk multi-server
- batas ukuran 4kb
- rentan XSS
- dapat dimanipulasi di sisi klien

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies tidak otomatis aman. Kita tetap memiliki risiko, seperti :
Risiko umum:
-XSS: script berbahaya bisa mencuri cookie jika bukan HttpOnly.
-CSRF: request sah tampak datang dari browser user.
-Session hijacking/fixation: pencurian/penyematan sessionid.
-Transport sniffing: tanpa HTTPS, cookie bisa disadap.
Cara untuk django menangani hal tersebut: 
-SESSION_COOKIE_HTTPONLY = True (default) berarti cookie session tidak bisa diakses JS.
-SESSION_COOKIE_SECURE = True di production berarti cookie hanya lewat HTTPS.
-PASSWORD_HASHERS (PBKDF2) berarti password tidak disimpan plaintext.
-Session server-side (default DB) berarti klien hanya memegang sessionid.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Membuat User Registration dengan menambahkan fungsi register di views.py menggunakan UserCreationForm, membuat file register.html, dan menambahkan routing di urls.py.

Membuat User Login dengan fungsi login_user yang menggunakan AuthenticationForm, serta menambahkan mekanisme session dan cookie last_login. Membuat template login.html yang rapi dan terpusat.

Membuat User Logout dengan fungsi logout_user yang menghapus session dan cookie, lalu mengarahkan kembali ke halaman login.

Menambahkan @login_required pada view show_main dan halaman lain yang butuh autentikasi, sehingga hanya pengguna yang sudah login yang bisa mengaksesnya.

Menghubungkan model Product dengan User dengan menambahkan field user = models.ForeignKey(User, ...) pada model. Mengubah create_product supaya produk yang dibuat otomatis terkait dengan request.user.

Menampilkan detail user yang sedang login di halaman utama (username dan waktu last_login dari cookie).

Membuat dua akun pengguna dan mengisi masing-masing tiga dummy data produk menggunakan halaman create product setelah login.

Melakukan add, commit, dan push ke GitHub dan PWS supaya perubahan tersimpan dan aplikasi dapat diakses secara online.

Jawaban pertanyaan Tugas 5
1) Urutan prioritas (specificity) jika ada banyak CSS selector yang menarget elemen yang sama
Urutan:
- !important pada deklarasi (hindari kecuali darurat).
- Inline style pada elemen (contoh: <div style="color:red">).
- Selector ID (#header, specificity ~ 0,1,0,0).
- Class / Attribute / Pseudo-class (.btn, [type="text"], :hover, specificity ~ 0,0,1,0).
- Element / Pseudo-element (h1, p, ::before, specificity ~ 0,0,0,1).
- Jika masih seri maka aturan paling bawah di file (deklarasi terakhir) yang menang

2) Kenapa responsive design penting? + contoh yang sudah & belum responsif
- Multi-device: layar HP, tablet, sampai desktop punya ukuran dan rasio beda.
- UX & aksesibilitas: navigasi tetap nyaman tanpa zoom/pinch.
- SEO & performa: Google mengutamakan mobile-friendly; layout adaptif biasanya lebih ringan.
- Maintainability: satu basis kode melayani banyak perangkat (ketimbang subdomain m-dot).

Contoh yang sudah responsif (umum):
GitHub / Wikipedia / Gmail (web), navigasi, grid, dan tipografi menyesuaikan lebar layar; sidebar berubah jadi menu.

Contoh yang belum responsif :
Dashboard legacy / aplikasi internal lama , tabel melebar keluar layar di HP, navbar pecah, butuh scroll horizontal.
Pada proyek ini, navbar dan halaman produk sudah dibuat responsif (grid kolom menyesuaikan breakpoint; navbar berubah ke hamburger fullscreen di mobile).

3) Perbedaan margin, border, dan padding + cara implementasi
- Margin: ruang di luar border; “jarak” antar elemen.
- Border: garis tepi yang “mengelilingi” konten + padding.
- Padding: ruang di dalam border; jarak teks/konten ke tepi box.

Contoh cara menerapkannya menggunakan css
.card {
  margin: 16px;               /* jarak antar kartu */
  border: 1px solid #e5e7eb;  /* garis tepi */
  padding: 12px;              /* ruang dalam kartu */
  border-radius: 8px;
}

4) Konsep Flexbox & Grid + kegunaannya
Flexbox (1D layout) :
- Fokus ke satu dimensi (baris atau kolom).
- Cocok untuk: navbar dengan item rata tengah & kanan, komponen kartu dengan tombol sejajar.
Grid (2D layout):
- Fokus ke dua dimensi (baris dan kolom).
- Cocok untuk: katalog produk, dashboard dengan sidebar + konten, layout majalah.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Membuat kerangka base.html sebagai layout utama, mengimpor CDN Tailwind, dan memastikan blok {% block content %} dipakai ulang di semua halaman.

Menata navbar agar menu Home/Produk/Tambah Produk berada di tengah dan area kanan menampilkan username + NPM/Kelas + Logout, tanpa mengubah warna/branding “Sidja”.

Menambahkan hamburger menu untuk mobile yang membuka fullscreen overlay navigasi; tombol × untuk menutup, serta menyembunyikan menu desktop pada breakpoint kecil.

Menambahkan context processor kustom agar student_npm dan student_class tersedia otomatis di semua template tanpa harus mengirim context satu-satu dari setiap view.

Membuat grid katalog produk yang responsif (kolom adaptif di sm/lg/xl), kartu produk dengan gambar, nama ter-truncate, harga, tombol Detail, serta tombol Edit/Delete yang hanya muncul untuk pemiliknya.

Menyusun ProductForm berbasis ModelForm dan memastikan field category memakai choices bertema toko football serta field is_featured tampil di form.

Membangun halaman Create Product dan Edit Product yang modern: label kecil, input rounded, fokus dengan ring, select kategori, checkbox featured, dan tombol aksi yang konsisten.

Menyempurnakan halaman Detail Product untuk menampilkan {{ product.get_category_display }}, badge “Featured” bila aktif, gambar (bila ada), dan author dengan fallback ke “Anonymous” bila tidak tersedia.

Mengamankan seluruh operasi dengan @login_required serta pembatasan kepemilikan (query pakai user=request.user), merapikan penamaan URL (main:...), dan memastikan view Delete selalu mengembalikan HttpResponseRedirect.

Menguji di lokal pada berbagai ukuran layar, memperbaiki error umum (mis. NoReverseMatch, TemplateDoesNotExist, dan return view), lalu commit & push ke GitHub serta deploy ke PWS, diakhiri pembaruan README.md.
