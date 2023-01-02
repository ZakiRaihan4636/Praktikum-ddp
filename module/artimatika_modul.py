# modul aritmatika 
def tambah(*angka):
    hasil = 0
    for ang in angka:
        hasil = hasil + ang
    for i in range(0, len(angka)):
        print(angka[i], "+", end=' ')
    print("=", hasil)
    


# modul aritmatika 
def kali(*angka):
    hasil = 1
    for ang in angka:
        hasil = hasil * ang
    for i in range(0, len(angka)):
        print(angka[i], "", end=' ')
    print("=", hasil)

def kurang(*angka):
    hasil = 0
    awal = True
    for i in angka:
        if awal:
            awal = False
            hasil = i
            continue
        hasil -= i
    return hasil

