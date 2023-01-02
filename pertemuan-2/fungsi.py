
def grade(nilai, nama, matkul):
  if nilai >= 85 and nilai <= 100:
    print("Nama Mahasiswa : ", nama)
    print("Matakuliah : ", matkul)
    print("Nilai : ", nilai)
    print("Grade Nilai : A")
  elif nilai >= 75 and nilai < 85:
    print("Nama Mahasiswa : ", nama)
    print("Matakuliah : ", matkul)
    print("Nilai : ", nilai)
    print("Grade Nilai : B")
  elif nilai >= 60 and nilai < 75:
    print("Nama Mahasiswa : ", nama)
    print("Matakuliah : ", matkul)
    print("Nilai : ", nilai)
    print("Grade Nilai : C")
  else:
    print("Nama Mahasiswa : ", nama)
    print("Matakuliah : ", matkul)
    print("Nilai : ", nilai)
    print("Grade Nilai : E")

grade(90, "Zaki", "DDP")