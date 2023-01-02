def kurang(*angka):
    hasil = 0
    for i in range(0, len(angka)):
        hasil = angka[i] - hasil
    print(-hasil)

kurang(1,2)