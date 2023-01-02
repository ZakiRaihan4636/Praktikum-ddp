# List makanan dengan 2 dimensi
list_makanan = [
  ["Bakwan", "Combro", "Mistro"],
  ["Sop Iga", "sop Buntut", "Sop Kaki"],
  ["Nasi Uduk", "Nasi Goreng", "Nasi Rames"]
]

print('--------- cetak per item -------- ')
print(list_makanan[0][0])
print(list_makanan[1][2])
print(list_makanan[2][2])

print('--------- cetak Semuanya dengan nestedLoop -------- ')
print("Menu makanan :")

for menu in list_makanan:
  for makanan in menu:
    print(makanan)
