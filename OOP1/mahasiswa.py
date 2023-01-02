class Mahasiswa:
  nim = ""
  nama = ""
  rombel = ""
  
  def __init__(self, nim, nama, rombel):
    self.nim = nim
    self.nama = nama
    self.rombel = rombel

  def welcome(self):
     print("Hallo", self.nama, "Di STT Terpadu Nurulfikri")

  def lulus(self, nilai):
    if(nilai > 90):
      return("lulus")
    else:
      return("tidak lulus")

mhs1 = Mahasiswa("01121110", "Muhamad Zaki Raihan", "TI04")
# mhs1.nama = "Zaki" 
# mhs1.nim = "0110221110" 
# mhs1.rombel = "TI04"

print("Nama mahasiswa", mhs1.nama)
print("NIM :",mhs1.nim)
print("Rombel :",mhs1.rombel)
print("lulus :",mhs1.lulus(91))





