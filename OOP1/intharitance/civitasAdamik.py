from Mahasiswa import *
from Dosen import *

mhs1 = Mahasiswa("Muhamad Zaki Raihan", "Laki-Laki", 20, "TI", 3)
dsn1 = Dosen("Reza Maulana", "Laki-Laki", 25, "S.si, M.Kom", "Ketua BTSI")

dsn1.setGaji(1200000)
mhs1.cetak()
dsn1.cetak()