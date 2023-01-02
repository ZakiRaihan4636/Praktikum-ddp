def konsonanOnly(kalimat):
  kalimat_baru = ""
  huruf_vokal = ["a","i","u","e","o", " "]
  for i in kalimat:
    if i not in huruf_vokal:
      kalimat_baru += i
  print(kalimat_baru)

konsonanOnly("STT Terpadu Nurulfikri")


