nama = "Muhamad Zaki Raihan"
matkul = "DDP"
nilai = 90

if(nilai >= 85 and nilai <= 100):
  grade = "A"
elif(nilai >= 75 and nilai < 85):
  grade = "B"
elif(nilai >= 60 and nilai < 75):
  grade = "C"
elif(nilai >= 30 and nilai < 60):
  grade = "D"
else:
  grade = "E"


print("Nama Mahasiswa    : ", nama)
print("Mata Kuliah       : ", matkul)
print("Nilai             : ",nilai)
print("Grade             : ",grade)

