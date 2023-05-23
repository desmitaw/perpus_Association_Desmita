# perpus_Association_Desmita
Program di atas mengimplementasikan sistem peminjaman buku di perpustakaan menggunakan konsep Association antara kelas Book dan LibraryMember. Berikut penjelasan detailnya:

Kelas Book:

Kelas ini merepresentasikan sebuah buku dalam perpustakaan.
Atribut title menyimpan judul buku.
Atribut author menyimpan penulis buku.
Atribut is_available adalah sebuah boolean yang menandakan status ketersediaan buku.
Metode borrow() digunakan untuk meminjam buku. Jika buku tersedia, maka status ketersediaan diubah menjadi False dan mengembalikan True. Jika buku sedang dipinjam, mengembalikan False.
Metode return_book() digunakan untuk mengembalikan buku. Mengubah status ketersediaan buku menjadi True.
Kelas LibraryMember:

Kelas ini merepresentasikan seorang anggota perpustakaan.
Atribut name menyimpan nama anggota perpustakaan.
Atribut borrowed_books adalah sebuah list yang berisi objek Book yang dipinjam oleh anggota.
Metode borrow_book() digunakan untuk meminjam buku. Jika buku dapat dipinjam, maka buku ditambahkan ke dalam daftar borrowed_books dan mencetak pesan yang menampilkan informasi buku yang dipinjam. Jika buku tidak tersedia, mencetak pesan bahwa buku tidak tersedia.
Metode return_book() digunakan untuk mengembalikan buku. Jika buku ada dalam daftar borrowed_books, maka buku dikembalikan dengan mengubah status ketersediaan buku dan menghapus buku dari daftar borrowed_books.
Metode display_borrowed_books() digunakan untuk menampilkan daftar buku yang dipinjam oleh anggota beserta informasi detailnya seperti judul, penulis, dan status ketersediaan.
Pada bagian utama program:

Objek LibraryMember dengan nama "John" dibuat.
Beberapa objek Book dibuat, yaitu book1, book2, dan book3.
Objek book1 dan book2 dipinjam oleh member1 menggunakan metode borrow_book().
Metode display_borrowed_books() dipanggil untuk menampilkan daftar buku yang dipinjam oleh member1.
Kemudian, book1 dikembalikan menggunakan metode return_book().
Metode display_borrowed_books() dipanggil kembali untuk menampilkan daftar buku setelah pengembalian.
Output yang dihasilkan:

Program mencetak pesan yang memberitahukan bahwa member1 telah meminjam book1 dan book2.
Metode display_borrowed_books() mencetak daftar buku yang dipinjam oleh member1 beserta informasi detailnya.
Setelah book1 dikembalikan, program mencetak pesan pengembalian buku.
Metode display_borrowed_books() kembali dipanggil dan mencetak daftar buku yang masih dipinjam oleh `
