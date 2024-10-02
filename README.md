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

13. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (lihat kembali langkah 10).
14. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :
    ```bash
    git branch -M main
    ```
15. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.
16. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2. Bagan _request client_ Django

![Bagan request Django](https://media.discordapp.net/attachments/1215508424339750952/1283263912166297651/IMG_20240911_101230.jpg?ex=66eaede6&is=66e99c66&hm=c0b3d47b5b58f067dab53e2ac4eb749bf3e907b14aa80d74754b1ab6f4d6a7d9&=&format=webp&width=916&height=591)

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

## Tugas Individu 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dalam pengimplementasian sebuah platform sangat penting karena memastikan bahwa data yang dihasilkan, diproses, dan disimpan oleh platform dapat sampai ke tujuan yang tepat, baik itu ke pengguna akhir, sistem lain, atau penyimpanan data, dengan cara yang efisien, aman, dan handal. Berikut adalah alasan mengapa kita memerlukan data delivery:

1. Platform biasanya terdiri dari berbagai komponen atau layanan yang harus berkomunikasi satu sama lain. Data delivery memastikan bahwa informasi dapat dipertukarkan antara komponen-komponen tersebut, baik secara lokal maupun melalui jaringan.

2. Data yang dikirimkan dengan cepat dan akurat meningkatkan pengalaman pengguna. Jika data tidak terkirim dengan baik atau tertunda, pengguna dapat mengalami gangguan seperti lambatnya aplikasi, kehilangan data, atau hasil yang tidak konsisten.

3. Proses pengiriman data sering melibatkan data sensitif seperti informasi pribadi atau transaksi keuangan. Dengan pengelolaan data delivery yang baik, keamanan seperti enkripsi dapat diterapkan untuk memastikan data tidak jatuh ke tangan yang salah selama proses pengiriman.

4. Sistem platform yang andal memerlukan mekanisme pengiriman data yang memastikan data tidak hilang atau rusak selama transfer, meskipun terjadi kegagalan jaringan atau kesalahan sistem. Data delivery yang handal termasuk dalam menyediakan mekanisme retry atau pengulangan pengiriman jika terjadi kegagalan.

5. Banyak platform modern yang memerlukan pemrosesan data secara real-time, seperti platform e-commerce, streaming media, atau sistem monitoring. Data delivery yang cepat dan efisien mendukung kebutuhan ini, sehingga memungkinkan respons yang cepat dan relevan terhadap pengguna.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik daripada XML dalam banyak konteks, terutama dalam pengembangan web modern dan integrasi API. JSON lebih sederhana, lebih efisien, dan lebih mudah dibaca, yang membuatnya menjadi pilihan utama dibandingkan XML. Alasan JSON lebih popular adalah karena JSON jauh lebih mudah dibaca oleh manusia karena tidak terlalu banyak elemen yang membebani. Dalam banyak kasus, pengembang hanya perlu melihat sedikit data JSON untuk memahami struktur dan kontennya, sementara XML sering kali terlihat terlalu bertele-tele dengan tag-tag yang mengelilingi setiap elemen. JSON menggunakan format yang lebih sederhana dan ringkas, dengan kurung kurawal ({}) dan kurung siku ([]) untuk menandai objek dan array, dibandingkan dengan XML yang memerlukan tag pembuka dan penutup seperti <name></name>. Ini membuat JSON lebih hemat ruang dan lebih mudah dibaca secara visual.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Dalam Django, method is_valid() pada sebuah form berfungsi untuk memeriksa apakah data yang dikirimkan ke form valid berdasarkan aturan yang telah didefinisikan. Method ini adalah salah satu bagian penting dari proses validasi form, yang memastikan bahwa data yang diterima sesuai dengan tipe dan aturan yang diinginkan sebelum diproses lebih lanjut, seperti menyimpan ke database atau mengirimkan respon ke pengguna.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah salah satu jenis serangan di mana penyerang dapat memaksa pengguna yang sudah terautentikasi untuk melakukan tindakan yang tidak diinginkan di aplikasi web tanpa sepengetahuan mereka. Jika kita tidak menambahkan CSRF token pada form di Django, aplikasi menjadi rentan terhadap serangan CSRF. Dalam skenario seperti ini, penyerang dapat memanfaatkan kerentanan tersebut dengan mengirimkan permintaan palsu atas nama pengguna yang sudah login. Misalnya, penyerang bisa membuat situs jahat yang ketika dikunjungi oleh pengguna, secara otomatis mengirimkan permintaan ke aplikasi yang mereka login tanpa disadari oleh pengguna. Akibatnya, tindakan berbahaya seperti pengubahan data atau transaksi finansial bisa terjadi. Tanpa CSRF token, server tidak dapat memverifikasi apakah permintaan tersebut berasal dari pengguna yang sah atau bukan, sehingga meningkatkan risiko serangan. Django secara otomatis menyediakan mekanisme CSRF ini sebagai tindakan pengamanan untuk memastikan bahwa setiap permintaan POST berasal dari sumber yang terpercaya, menjaga integritas dan keamanan aplikasi dari eksploitasi yang tidak diinginkan.

## Tugas Individu 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?

`HttpResponseRedirect()`
- Kelas Django yang merupakan turunan dari `HttpResponse`.
- Kita harus memberikan URL secara manual
- Sintaks nya :

    ```python
    from django.http import HttpResponseRedirect

    def my_view(request):
        return HttpResponseRedirect('/some-url/')
    ```

`redirect()`
- Fungsi shortcut yang disediakan oleh Django.
- Lebih sederhana dan fleksibel karena dapat menerima berbagai jenis argumen, seperti URL, nama pola URL (URL pattern name), atau objek model.
- Sintaks nya :

    ```python
    from django.shortcuts import redirect

    def my_view(request):
        return redirect('/some-url/')  # Bisa dengan URL langsung
    ```

Kesimpulannya adalah `HttpResponseRedirect()` digunakan ketika kita ingin mengarahkan pengguna ke URL tertentu yang kita tentukan secara eksplisit dan `redirect()` adalah versi yang lebih fleksibel dan user-friendly karena dapat menerima URL, pola URL, atau objek model. `redirect` lebih sering digunakan karena lebih mudah dan fleksibel.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!

Dalam Django, untuk menghubungkan model Product dengan model User, kita biasanya menggunakan foreign key. Penghubungan ini memungkinkan setiap produk dikaitkan dengan pengguna tertentu, yang biasanya adalah pembuat, pemilik, atau pengelola produk tersebut.

**1. Menghubungkan `product` dan `user` di models.py**
Melakukan import `User` dengan `django.contrib.auth.models` di models.py. Berikut contoh di dalam koding saya.

    ```python
    from django.db import models
    import uuid
    from django.contrib.auth.models import User

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        quantity = models.IntegerField(default=0)

        @property
        def  is_available(self):
            return  self.quantity > 0
    ```

**2. Menghubungkan dengan `create_product` di views.py**
Dalam model `Product`, kita menambahkan foreign key yang menghubungkan `Product` dengan `User`. Berikut contoh di dalam koding saya.

    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST" :
            product_entry = form.save(commit = False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')

        context = {'form': form}

        return render(request, "create_product.html", context)
    ```

**3. Filter produk pada `show_main` di views.py**
Filter produk berdasarkan pengguna yang sedang login menggunakan `Product.objects.filter(user=request.user)`. Berikut contoh di dalam koding saya.

    ```python
    @login_required(login_url='/login')
    def show_main(request):
        isi_product = Product.objects.filter(user=request.user)
        context = {
            'app' : 'FShop',
            'npm': '2306226731',
            'name': request.user.username,
            'class': 'PBP C',
            'products' : isi_product,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)
    ```

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Perbedaan antara Authentication dan Authorization:**
1. Authentication (Otentikasi):
Authentication adalah proses memverifikasi identitas pengguna. Dengan kata lain, ini adalah proses memastikan bahwa pengguna adalah siapa yang mereka klaim. Biasanya melibatkan memeriksa kredensial seperti username dan password. Contohnya, ketika pengguna memasukkan username dan password mereka ke dalam sistem, sistem memverifikasi apakah kredensial tersebut cocok dengan yang ada di database.

2. Authorization (Otorisasi):
Authorization adalah proses memberikan atau membatasi akses ke sumber daya tertentu berdasarkan identitas pengguna yang telah diotentikasi. Jadi, setelah pengguna berhasil diotentikasi, otorisasi menentukan apakah mereka memiliki izin untuk mengakses fitur atau data tertentu. Contohnya, setelah pengguna berhasil login, sistem memeriksa apakah pengguna tersebut memiliki hak akses untuk mengedit data atau hanya melihat data tertentu.

**Impplementasi Authentication dan Authorization:**
1. Authentication (Otentikasi):
Implementasinya di dalam koding saya adalah sebagai berikut.

    ```python
    from django.http import HttpResponseRedirect
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```
2. Authorization (Otorisasi):
Implementasinya di dalam koding saya adalah sebagai berikut.

    ```python
    @login_required(login_url='/login')
    def show_main(request):
        isi_product = Product.objects.filter(user=request.user)
        context = {
            'app' : 'FShop',
            'npm': '2306226731',
            'name': request.user.username,
            'class': 'PBP C',
            'products' : isi_product,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)
    ```

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login menggunakan cookies dan session. Proses ini bekerja sebagai berikut:

1. Session ID di Cookies:
Ketika pengguna login, Django membuat session untuk pengguna tersebut dan menyimpan data session di database (atau tempat lain yang diatur, misalnya cache atau file system). Django kemudian mengirimkan sebuah session ID yang unik kepada browser pengguna dalam bentuk cookie. Cookie ini biasanya bernama sessionid secara default. Pada setiap request berikutnya, browser pengguna mengirimkan cookie ini kembali ke server Django, sehingga server dapat mengidentifikasi pengguna yang sedang login dengan mencocokkan session ID di cookie dengan session yang disimpan di server.

2. Session di Server:
Data session yang terkait dengan session ID disimpan di sisi server. Data ini berisi informasi seperti apakah pengguna sudah login, serta objek pengguna (user object) yang terkait. Django menyediakan modul django.contrib.sessions yang mengelola sesi ini secara otomatis. Setiap kali pengguna membuat request, Django memeriksa session untuk melihat apakah pengguna sudah login dengan memvalidasi session ID dari cookie.

**Kegunaan Lain dari Cookies**
Cookies bukan hanya digunakan untuk mengingat pengguna yang telah login. Berikut beberapa kegunaan lain dari cookies:

1. Preferensi Pengguna:
Cookies dapat menyimpan pengaturan atau preferensi pengguna seperti tema situs (gelap/terang), bahasa, ukuran teks, atau preferensi tampilan lainnya.

2. Pelacakan dan Analisis:
Banyak situs web menggunakan cookies untuk melacak aktivitas pengguna di situs mereka untuk analisis dan peningkatan pengalaman pengguna. Google Analytics adalah salah satu contoh layanan yang menggunakan cookies untuk melacak perilaku pengguna.

3. Personalized Advertising:
Cookies digunakan untuk menampilkan iklan yang disesuaikan dengan preferensi pengguna berdasarkan perilaku mereka sebelumnya di internet. Ini termasuk pelacakan di banyak situs web melalui pihak ketiga (third-party cookies).

4. Shopping Cart:
Dalam aplikasi e-commerce, cookies dapat digunakan untuk mengingat barang yang pengguna tambahkan ke dalam keranjang belanja, bahkan jika pengguna belum login.

5. Session Persistence:
Seperti dijelaskan di atas, cookies sering digunakan untuk menjaga sesi login pengguna, sehingga mereka tidak perlu login berulang kali.

**Apakah Semua Cookies Aman Digunakan?**
Tidak semua cookies aman digunakan. Meskipun cookies sangat berguna, ada beberapa risiko keamanan yang harus diperhatikan:

1. Cross-Site Scripting (XSS):
Cookies yang tidak dilindungi dengan benar dapat menjadi target serangan XSS, di mana penyerang dapat menyuntikkan kode jahat yang memungkinkan mereka mencuri cookies, termasuk session ID. Hal ini dapat memungkinkan penyerang mengakses akun pengguna yang login.
Untuk mencegahnya, cookies yang menyimpan informasi sensitif harus diberi atribut HttpOnly agar tidak dapat diakses oleh JavaScript.

2. Cross-Site Request Forgery (CSRF):
Cookies bisa digunakan dalam serangan CSRF, di mana penyerang memanfaatkan sesi pengguna yang sudah login untuk melakukan aksi berbahaya di situs tanpa sepengetahuan pengguna.
Django mengatasi ini dengan menerapkan perlindungan CSRF secara otomatis menggunakan token yang unik dalam setiap request POST atau aksi berisiko lainnya.

3. Third-Party Cookies:
Cookies pihak ketiga (third-party cookies) yang digunakan untuk pelacakan antar situs bisa menimbulkan risiko privasi. Informasi ini sering digunakan oleh jaringan iklan untuk melacak perilaku pengguna di berbagai situs web dan membangun profil pengguna tanpa izin eksplisit.
Banyak browser modern kini mulai memblokir third-party cookies untuk melindungi privasi pengguna.

4. Cookie Hijacking:
Jika cookies dikirim tanpa enkripsi (misalnya melalui HTTP, bukan HTTPS), mereka bisa dicegat oleh pihak ketiga yang melakukan serangan man-in-the-middle. Oleh karena itu, cookies harus selalu dikirim melalui koneksi yang aman dengan mengaktifkan atribut Secure, sehingga cookies hanya dikirim melalui HTTPS.

5. Cookie Overload:
Terlalu banyak menggunakan cookies dapat membebani bandwidth dan memperlambat situs web, terutama jika data yang disimpan dalam cookie besar dan tidak dikelola dengan baik.

## Tugas Individu 5

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

1. Inline styles, yaitu CSS yang ditulis langsung pada elemen HTML menggunakan atribut `style=""` akan selalu memiliki prioritas tertinggi.

Contoh: 
`<div style="color: red;"></div>`

2. ID selectors, yaitu selektor yang merujuk ke elemen berdasarkan atribut `id`. Setiap kali selektor menggunakan `#id`, ia lebih kuat dibandingkan kelas atau elemen.

Contoh:
`#header { color: blue; }`
    

3. Class selectors, attribute selectors, dan pseudo-class selectors, yaitu selektor yang menggunakan kelas `(.class)`, atribut `([type="text"])`, atau pseudo-class (`:hover`, `:focus`, dll.) memiliki prioritas lebih rendah daripada ID, tetapi lebih tinggi daripada elemen.
    

Contoh:
`.btn { color: green; }`
`[type="text"] { background: yellow; }`
`a:hover { text-decoration: underline; }`

4. Element selectors dan pseudo-elements, yaitu selektor yang merujuk ke elemen HTML (misalnya `div`, `p`, `h1`, dll.) dan pseudo-elemen seperti `::before`, `::after` memiliki prioritas paling rendah.

Contoh:
`p { font-size: 16px; }`
`::before { content: ''; }`

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memastikan bahwa aplikasi atau situs web dapat beradaptasi dengan berbagai ukuran layar dan perangkat (seperti ponsel, tablet, dan desktop). Hal ini berguna untuk memberikan pengalaman pengguna yang optimal tanpa harus membuat versi terpisah untuk setiap jenis perangkat.
Contoh aplikasi yang sudah menerapkan responsive design :

1. **YouTube**, menyesuaikan tampilan video dan elemen navigasi berdasarkan ukuran layar. Di desktop, YouTube menampilkan sidebar dan tata letak lebar, sementara pada perangkat mobile, tata letaknya berubah menjadi lebih vertikal dan elemen-elemen menjadi lebih besar untuk kemudahan sentuhan.

2. **Spotify**, menyediakan tampilan yang responsif untuk platform web-nya. Ketika diakses melalui desktop, tampilan lebih lengkap dengan kontrol yang lebar dan sidebar navigasi. Pada perangkat mobile, elemen-elemen seperti tombol play, pause, dan navigasi lagu lebih besar dan mudah dijangkau dengan jari.

Contoh aplikasi yang belum menerapkan responsive design :

1. Situs Web Toko Online Lama, yang masih menggunakan desain lama mungkin belum responsif. Pengguna harus melakukan zoom in/out dan scroll horizontal saat mengakses dari perangkat mobile, yang sangat mengurangi pengalaman pengguna.

2. Situs Web Katalog PDF Statis, yang hanya menampilkan katalog dalam format PDF tanpa adaptasi terhadap ukuran layar sering kali tidak responsif. Pengguna perlu membuka dan membaca PDF dengan kesulitan pada perangkat mobile karena tidak ada penyesuaian elemen.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

1. **Margin**, adalah ruang di luar elemen yang memisahkan elemen tersebut dari elemen lain. Ini merupakan jarak antara batas luar elemen dengan elemen-elemen di sekitarnya. Cara kerjanya margin tidak memengaruhi ukuran elemen, tetapi memengaruhi jarak elemen dengan elemen lain. Margin juga dapat menggunakan nilai positif atau negatif. Contoh implementasinya :

    ```bash
    div {
        margin: 20px; /* Semua sisi (atas, kanan, bawah, kiri) memiliki margin 20px */
        margin-top: 10px; /* Margin atas 10px */
        margin-right: 15px; /* Margin kanan 15px */
        margin-bottom: 10px; /* Margin bawah 10px */
        margin-left: 15px; /* Margin kiri 15px */
    }
    ```
2. **Border**, adalah garis yang mengelilingi elemen dan ditempatkan di antara padding dan margin. Border membentuk batas visual dari elemen dan bisa diberi warna, ketebalan, serta gaya (solid, dashed, dotted, dll.). Cara kerjanya border berada tepat di luar padding dan di dalam margin. Border dapat dikustomisasi dengan berbagai gaya dan ukuran. Contoh implementasinya :

    ```bash
    div {
        border: 2px solid black; /* Border dengan ketebalan 2px, gaya solid, warna hitam */
        border-top: 1px dashed red; /* Border atas bergaris putus-putus (dashed) dengan warna merah */
    }

3. **Padding**, adalah ruang di dalam elemen antara konten elemen (misalnya teks atau gambar) dan batas (border) elemen. Padding memberikan jarak antara konten elemen dengan batas elemen. Cara kerjanya padding ialah memperluas ukuran elemen, karena menambah jarak di dalam elemen tanpa memengaruhi posisi elemen lain. Tidak seperti margin, padding tidak bisa memiliki nilai negatif. contoh implementasinya :

    ```bash
    div {
        padding: 20px; /* Semua sisi memiliki padding 20px */
        padding-top: 10px; /* Padding atas 10px */
        padding-right: 15px; /* Padding kanan 15px */
        padding-bottom: 10px; /* Padding bawah 10px */
        padding-left: 15px; /* Padding kiri 15px */
    }

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

**Flexbox** adalah sistem layout yang dirancang untuk mengatur elemen secara linear dalam satu dimensi, baik itu secara horizontal (row) atau vertikal (column). Flexbox sangat berguna ketika kita ingin membuat tata letak yang fleksibel dan dinamis untuk elemen dalam satu baris atau kolom.

Kegunaan Flexbox:
1. Flexbox sangat baik digunakan untuk membuat tata letak elemen dalam satu dimensi, seperti navbar horizontal, sidebar vertikal, atau layout kartu-kartu produk.
2. Kita bisa membuat elemen menyesuaikan lebar atau tinggi berdasarkan ruang yang tersedia, sehingga tata letak tetap responsif dan adaptif tanpa memerlukan pengukuran piksel tetap.

**Grid Layout** adalah sistem tata letak dua dimensi (dua arah) yang lebih canggih daripada Flexbox. Dengan Grid, kita bisa mengatur elemen dalam baris (rows) dan kolom (columns) secara bersamaan, membuatnya lebih cocok untuk tata letak yang kompleks seperti halaman web yang memiliki header, footer, sidebar, dan konten utama.

Kegunaan Grid Layout:
1. Grid ideal untuk tata letak yang membutuhkan pengaturan elemen dalam baris dan kolom, seperti dashboard, majalah digital, atau halaman blog dengan beberapa konten.
2. Grid memberikan kontrol penuh terhadap ukuran dan posisi setiap elemen dalam grid, memungkinkan kita untuk mengatur layout yang lebih kompleks dibandingkan Flexbox.
3. Grid dapat dengan mudah digunakan untuk membuat struktur utama halaman, seperti header, sidebar, konten, dan footer.