class Gempa:
  def __init__(self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala

  def dampak(self):
    if(self.skala < 2):
      ket = "tidak berasa"
    elif(self.skala >= 2 and self.skala < 4):
      ket = "bangunan retak retak"
    elif(self.skala <= 4 and self.skala < 6):
      ket = "Bangunan pada roboh"
    else:
      ket = "Berpotensi tsunami"
    print("Terjadi gempa di", self.lokasi, "dengan skala", self.skala, "richter", "berdampak", ket)
  
g1 = Gempa("banten", 1.4)
g2 = Gempa("Tokyo", 7)

g1.dampak()
g2.dampak()
