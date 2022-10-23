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

