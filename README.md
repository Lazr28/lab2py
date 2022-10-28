# Latihan Python

Untuk memulai latihan bahasa python, kita perlu menginstall program programnya.
anda bisa mendownload pada link berikut https://www.python.org/downloads/

![Screenshot Halaman Download](/Screenshot/SS-download.png)

Setelah selesai mendownload buka program installan tersebut


![Tampilan program installan](/Screenshot/SS-instal.png)

> Centang Add python.exe to PATH agar python dapat di panggil atau di jalankan melalui CMD / powershell.

kemudian klik **Install Now**


setelah selesai menginstall kita melanjutkan ke latihan pada materi.

## Latihan 1

buka cmd / powershell
lalu ketikan `python` kemudian enter

![Latihan 1 - masuk program python](/Screenshot/SS-Latihan%201-0.png)

untuk menampilkan teks 
> Hello, \
> Saya sedang belajar python

kita akan menggunakan sintaks `print("isi teksnya")`\
ketikan sintaks berikut pada cmd/ powershell.
```
print("hello")
print("Saya sedang belajar python")
```
maka tampilannya akan seperti berikut
![Latihan 1 - menampilkan teks](/Screenshot/SS-Latihan%201-1.png)


## Latihan 2

pada latihan ke 2 kita akan menjumlahkan dua buah bilangan menggunakan 2 variabel

untuk itu kita perlu mendefinisikan kedua variabel tersebut beserta nilainya.
>Contoh :\
>namaVariabel = nilai

pada latihan 2 kita akan menggunakan a dan b untuk nama variabelnya.


kita akan gunakan sintaks berikut pada Latihan ke 2 ini
```
a=8
b=6
print("variabel a=",a)
print("variabel b=",b)
print("hasil penjumlahan a+b=",a+b)

```

hasil dari sintaks diatas adalah seperti berikut
![Latihan 2 - menjumlahkan dua buah bilangan](/Screenshot/SS-Latihan%202-1.png)

> untuk menampilkan nilai dari variabel\
kita bisa menggunakan perintah `print("")`\
tetapi nama variabel tidak berada di dalam kutip "
![latihan 2 - menampilkan nilai variabel](/Screenshot/SS-Latihan%202-2.png)\
jika kita menggunakan kutip dua ( " ) untuk menambahkan teks maka kita perlu menggunakan koma ( , ) setelah kutip dua ( " ).\
kita juga bisa menjumlahkan langsung variabel tersebut 
seperti pada perintah sebelumnya.



## Latihan 3

Pada latihan ke 3 kita akan menggunakan aplikasi **IDLE**
dan akan menggunakan fungsi input pada program yang akan kita buat


\
buka aplikasi IDLE\
kemudian buat file baru dengan nama `latihan3.py`\
(pastikan file tersebut tersimpan di folder lab2py)\

untuk menginput 


\
kita akan gunakan sintaks berikut pada latihan ke 3:

```
# input nilai variabel
a = input("Masukan  nilai a: ")
b = input("Masukan  nilai b: ")

# cetak nilai variabel 
print("Variabel a =",a)
print("Variabel b =",b)

# cetak hasil operasi kedua variabel dengan string format
print("Hasil penggabungan {1}&{0}= %s ".format(a,b) %(a+b))

#konversikan nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1} + {0} = %d".format(a,b)  %(a+b))
print("Hasil pembagian {1} / {0} = %d".format(a,b)  %(a/b))

```


hasilnya akan seperti ini
![Latihan 3 - Menggunakan fungsi input](/Screenshot/SS-Latihan%203-0.png)

