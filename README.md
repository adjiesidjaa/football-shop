Link Domain : https://adjie-m-footballshop.pbp.cs.ui.ac.id/
Link Repo Github : https://github.com/adjiesidjaa/football-shop

Jawaban Pertanyaan

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

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

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
ada di file bagan penjelasan req client.png


Jelaskan peran settings.py dalam proyek Django!
settings.py itu pusat kendali satu projek di django. Semua konfigurasi inti yang nyambung ke semua hal di projek ditaruh di situ untuk jadi tempat buat ngatur semuanya. Singkatnya, settings.py itu blueprint environment yang membuat aplikasi dapat berjalan sesuai mode (dev dan production) tanpa perlu mengubah kode logika di app.

Bagaimana cara kerja migrasi database di Django?
Pertama, kita buat/mengubah model yang sudah ada
Kedua, kita menjalankan makemigrations yang membuat django membuat file migrasi otomatis
Ketiga, menjalankan migrate. File migrasi yang telah dibuat tadi dieksekusi, membuat tabel baru atau update kolom yang berubah.
Semua langkah ini dicatat oleh django historinya, jadi urutannya terlihat jelas dan dapat di-rollback kalau dibutuhkan.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Saya rasa, alasan Django dijadikan sebagai permulaan pembelajaran karena kita telah mempelajari python terlebih dahulu sebelumnya. Selain itu, django sudah cukup lengkap buat pemula yang belum mengerti mengenai pengembangan perangkat lunak. Django juga tidak terlalu ribet untuk setupnya, tetapi tetap memiliki fitur yang banyak.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Untuk sekarang, belum ada.
