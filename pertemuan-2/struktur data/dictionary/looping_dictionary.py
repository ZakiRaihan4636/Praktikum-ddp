mahasiswa = {
  "nama": "Muhamad Zaki Raihan",
  "matkul": "Dasar Pemrograman",
  "nilai" : 90
}

# looping nilai (values)
for i in mahasiswa.values():
  print(i)

# looping kata kunci (keys)
for j in mahasiswa.keys():
  print(j)

for key, values in mahasiswa.items():
  print(key, ":", values)
