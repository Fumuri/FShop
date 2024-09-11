# FShop

**_Dibuat oleh Muhammad Fakhri dengan NPM 2306226731 dari kelas PBP C_**

## Tugas Indvidu 2

### 1. Proses Pembuatan Tugas

#### Bagian 1, membuat projek Django baru

1. Membuat sebuah direktory baru bernama `FShop` di lokal
2. Membuat  _repository_ baru di Github dengan nama sama yaitu `FShop` dengan visibility _public_
3. Buka _command prompt_ dengan mengarah ke direktori 'Fshop'
4. Buat _virtual enviroment_ menggunakan python dengan command :

   ```bash
   python -m venv env
   ```

5. Mengaktifkan _virtual environement_ dengan command :

   ```bash
   env\Scripts\activate
   ```

6. _Virtual environment_ akan aktif yang ditandai (env) di awal baris input terminal
7. Membuat file `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ berikut :

   ```text
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```

8. Melakukan instalansi _dependencies_ pada `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

9. Buatlah projek Django baru dengan nama `FShop` :

   ```bash
   django-admin startproject FShop .
   ```

- Note : `.` harus tertulis di baris command

10. Mengubah isi variabel `ALLOWED_HOSTS` di file `settings.py` dengan kode berikut :

    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```

11. Pastikan bahwa file manage.py ada pada direktori yang aktif pada terminal kamu saat ini. Jalankan server Django dengan perintah :

    ```bash
    python manage.py runserver
    ```

12. Buka link [http://localhost:8000](http://localhost:8000/) pada peramban web untuk melihat animasi roket sebagai tanda aplikasi Django kamu berhasil dibuat.
13. Hentikan server dengan cara menekan `Ctrl+C` pada command
14. Non aktifkan virtual environment (env) :

    ```bash
    deactivate
    ```

#### Bagian 2, membuat aplikasi `main` dan melakukan _routing_

1. Membuat aplikasi baru dengan nama `main` dengan perintah berikut di command :

    ```bash
    python manage.py startapp main
    ```

2. Buka file `settings.py` di dalam direktori projek `FShop`dan tambahkan `'main'` ke dalam variabel `INSTALLED_APPS` seperti contoh berikut :

    ```python
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```

3. Buka file `urls.py` di dalam direktori proyek `FShop`, **bukan yang ada di direktori `main`.**
4. Lakukan perubahan pada isi file tersebut dengan kode berikut :

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

#### Bagian 3, membuat model pada aplikasi `main` dengan nama `Product` dan atribut wajib

1. Buka `manage.py` pada direktori `main`
2. Mengisi `manage.py` dengan kode berikut :

    ```python
    from django.db import models
    
    class Drink(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
    ```

3. Jalankan perintah berikut untuk membuat migrasi model :

    ```bash
    python manage.py makemigrations
    ```

4. Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal :

    ```bash
    python manage.py migrate
    ```

- Note: Setiap ada perubahan di `models.py`, lakukan langkah 3 dan 4 kembali.

#### Bagian 4, membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

1. Buka file `views.py` yang terletak pada direktori `main`.
2. Ubah isi file tersebut dengan kode berikut :

    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app' : 'FShop',
            'name': 'Muhammad Fakhri',
            'class': 'PBP C'
        }

        return render(request, "main.html", context)
    ```

3. Buat direktori baru bernama `templates` dalam direktori `main`.
4. Di dalam direktori `templates`, buat file baru dengan nama `main.html`. Isi file `main.html` dengan kode berikut :

    ```html
    <h1>{{ app }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>
    <h5>Class:</h5>
    <p>{{ class }}</p>
    ```

#### Bagian 5, membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`

1. Buat file baru bernama `urls.py` di  direktori main.
2. Isi file tersebut dengan kode berikut :

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

#### Bagian 6, testing projek

1. Di direktori `main`, buka file `tests.py`.
2. Isi file dengan kode berikut :

    ```python
    from django.test import TestCase, Client
    from .models import Product

    class mainTest(TestCase):
        def test_main_url_is_exist(self):
            response = Client().get('')
            self.assertEqual(response.status_code, 200)

        def test_main_using_main_template(self):
            response = Client().get('')
            self.assertTemplateUsed(response, 'main.html')

        def test_nonexistent_page(self):
            response = Client().get('/sapalah/')
            self.assertEqual(response.status_code, 404)

        def test_available(self):
            product = Product.objects.create(
              name="Buku",
              description="Campus",
              price = 100000,
            )
            self.assertTrue(product.is_available)
    ```

3. Jalankan file tes menggunakan perintah berikut :
    ```bash
    python manage.py test
    ```
4.. Jika tes berhasil dan aman, maka akan muncul informasi berikut :

    ```bash
    Found 4 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..
    ----------------------------------------------------------------------
    Ran 4 tests in 0.016s

    OK
    Destroying test database for alias 'default'...
    ```

#### Bagian 7, melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

###### ADD, COMMIT, PUSH GITHUB :

1. Lakukan inisiasi direktori lokal `FShop` sebagai repositori git dengan menjalankan perintah berikut pada terminal :
    ```bash
    git init
    ```
2. Kemudian, tandai semua _file_ yang berada pada direktori tersebut sebagai _file_ yang akan di-_commit (tracked)_ dengan perintah berikut :
    ```bash
    git add .
    ```
3. Lanjutkan membuat pesan _commit_ yang sesuai dengan perubahan atau pembaharuan dengan perintah berikut :
    ```bash
    git commit -m "<PESAN KAMU>"
    ```
4. Pastikan saat ini kamu berada pada branch _main_ dengan menjalankan perntah berikut :
    ```bash
    git branch -M main
    ```
5. Hubungkan repositori lokal (direktori saat ini) dengan repositori di Github kamu dengan perintah berikut :
    ```bash
    git remote add origin <URL_REPO>
    ```

- Note : ubah `<URL_REPO>` dengan url github yang baru kamu buat.

6. Kemudian, push seluruh file ke repositori github dengan perintah berikut :
    ```bash
    git push -u origin main
    ```

###### PUSH PWS :

7. Buka halaman PWS pada https://pbp.cs.ui.ac.id/ , kemudian buatlah akun atau _Register_ menggunakan akun SSO kamu.
8. Lakukan _login_ menggunakan akun yang baru saja kamu buat.
9. Buatlah proyek baru dengan menekan tombol `Create New Project`. Kamu akan berpindah ke halaman untuk membuat proyek baru. Silahkan isi `Project Name` dengan FShop. Setelah itu, tekan tombol `Create New Project` yang berwarna biru.
10. Simpan informasi _Project Credentials_ di tempat yang dan pastikan tidak hilang karena akan digunakan di langkah selanjutnya. **Jangan jalankan dulu instruksi _Project Command_.**
11. Lakukanlah update pada file `settings.py` di proyek Django kamu, tambahkan URL _deployment PWS_ pada variabel `ALLOWED_HOSTS` seperti kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "urls pws"]
    ...
    ```

- Note : ganti  sesuai dengan di pws.

12. Jalankan perintah berikut untuk melakukan push repositori lokal ke PWS kamu (jalankan satu per satu tiap baris) :

    ```bash
    git remote add pws http://pbp.cs.ui.ac.id/<USERNAME PWS>/fshop

    git branch -M master

    git push pws master
    ```

13. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (ingat kembali langkah 45).
14. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :
    ```bash
    git branch -M main
    ```
15. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.
16. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2. Bagan _request client_ Django

![Bagan request Django](https://cdn.discordapp.com/attachments/1215508424339750952/1283263912166297651/IMG_20240911_101230.jpg?ex=66e25c26&is=66e10aa6&hm=814fa472fe2734a6542daf19af641a2c016ad7ea2841fdfa8c25e434e8d45d76&)

Bagan di atas menjelaskan siklus request-response dalam aplikasi web Django. Berikut penjelasan tentang hubungan antara urls.py, views.py, models.py, dan berkas HTML dalam proses tersebut:

1. Permintaan Klien (Client Request): Proses dimulai ketika klien (biasanya browser atau aplikasi lain) mengirim permintaan ke server.
2. urls.py: Berkas ini berperan sebagai pengatur rute (routing) dalam aplikasi Django. urls.py menentukan URL yang sesuai dengan permintaan dan view yang akan menanganinya. Django mencocokkan URL dari permintaan dengan pola yang telah didefinisikan di urls.py.
3. views.py: Setelah urls.py menentukan view yang tepat, permintaan akan diteruskan ke fungsi atau kelas di views.py. Di sinilah data diproses, dan respons yang sesuai disiapkan untuk klien, yang mungkin melibatkan interaksi dengan model.
4. models.py: Jika view membutuhkan data dari database, ia akan berinteraksi dengan models.py. Di sini, struktur data dan manajemen basis data seperti pengambilan, penambahan, atau pengeditan data didefinisikan.
5. Database: Menyimpan dan menyediakan data yang diambil atau diperbarui oleh aplikasi.
6. models.py: Data yang diperoleh dari database dikembalikan ke models.py, kemudian diteruskan ke views.py.
7. views.py: Setelah mendapatkan data dari model, view akan memprosesnya dan menyiapkan konten, biasanya berkas HTML, untuk dikirim kembali ke klien.
8. HTML Template: Templat HTML diisi dengan data atau konteks yang disediakan oleh view dan kemudian di-render menjadi HTML lengkap yang siap dikirim ke klien.
9. Respons Klien (Client Response): HTML yang sudah di-render dikirim kembali ke klien sebagai respons atas permintaan yang mereka buat.

### 3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

Git adalah alat yang digunakan oleh developer dan programmer sebagai sistem kontrol versi dalam pengembangan perangkat lunak. Fungsinya adalah untuk mengelola versi kode sumber, memungkinkan penambahan atau perubahan kode dengan lebih terstruktur. Git pertama kali dikembangkan oleh Linus Torvalds pada tahun 2005.

Berikut beberapa fungsi Git dalam pengembangan perangkat lunak:

1. Kontrol Versi: Git memungkinkan penyimpanan berbagai versi proyek, baik versi lama maupun yang terbaru. Ini memudahkan developer untuk kembali ke versi sebelumnya jika ada masalah pada versi terbaru dari software atau aplikasi.
2. Kolaborasi: Git memfasilitasi kerja sama tim di antara para developer. Beberapa developer bisa bekerja secara bersamaan pada proyek yang sama tanpa saling mengganggu, dan Git membantu mengelola serta menggabungkan (merge) perubahan dari setiap developer dengan efisien.
3. Pelacakan Perubahan: Git mencatat setiap perubahan yang terjadi pada kode sumber, termasuk siapa yang membuat perubahan, kapan perubahan dilakukan, dan detail apa yang diubah.
4. Pengembangan Paralel: Git mendukung pembuatan cabang (branch), yang memungkinkan pengembang untuk bekerja pada fitur baru atau perbaikan bug secara terpisah dari kode utama. Cabang ini bisa digabungkan kembali ke kode utama setelah selesai.
5. Pemulihan: Dengan menyimpan semua versi kode, Git memudahkan developer untuk mengembalikan kode ke versi sebelumnya jika terjadi kesalahan atau kehilangan data.
6. Kemudahan Penggunaan: Git meskipun memiliki fitur kontrol versi yang canggih, dirancang untuk tetap mudah digunakan, sehingga developer bisa fokus pada pengembangan tanpa terbebani oleh pengelolaan perubahan kode.
7. Integrasi dengan Alat Lain: Git dapat terintegrasi dengan platform pengembangan lain seperti GitHub, GitLab, Bitbucket, serta alat pelacakan masalah.
8. Kinerja Tinggi: Git memberikan kinerja yang cepat dan efisien, bahkan dalam proyek yang memiliki riwayat panjang atau banyak cabang.
Secara keseluruhan, Git sangat bermanfaat dalam pengembangan perangkat lunak karena memungkinkan kolaborasi tim dan pengelolaan perubahan kode secara efektif dan efisien.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django sering dipilih sebagai framework awal untuk belajar pengembangan perangkat lunak karena beberapa alasan. Pertama, Django itu _batteries-included_, jadi banyak fitur bawaan yang siap pakai, misalnya otentikasi, ORM, dan admin interface. Ini sangat memudahkan pemula karena mereka nggak perlu mengonfigurasi banyak hal dari awal, bisa langsung fokus pada pengembangan logika aplikasi.

Selain itu, dokumentasinya sangat komprehensif dan mudah dipahami. Bagi pemula, ini penting banget, karena dokumentasi yang bagus bisa jadi referensi utama ketika bingung atau stuck.

Terus, Django juga mengikuti arsitektur yang jelas, yaitu **Model-View-Template (MVT)**, mirip dengan MVC. Struktur ini membantu pemula memahami bagaimana memisahkan logika aplikasi, data, dan tampilan dengan baik. Kombinasi fitur, dokumentasi, dan arsitektur yang rapi inilah yang bikin Django jadi framework yang bagus untuk mulai belajar pengembangan perangkat lunak.

### 5. Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis langsung perintah SQL.

Secara sederhana, ORM mengonversi tabel dan baris dalam database ke dalam bentuk objek di dalam kode Python. Setiap model Django mewakili tabel di database, dan setiap atribut di dalam model mewakili kolom dari tabel tersebut. Dengan ORM, kita bisa melakukan operasi database seperti create, read, update, dan delete (CRUD) menggunakan metode Python, sehingga lebih intuitif dan tidak perlu mempelajari sintaks SQL secara langsung.

Intinya, ORM di Django membuat proses manipulasi data dalam database lebih mudah dan lebih terintegrasi dengan bahasa pemrograman yang digunakan.