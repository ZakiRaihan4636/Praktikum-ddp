class mobil:
  def __init__(self, tipe, roda, kecepatan):
    self.tipe = tipe
    self.roda = roda
    self.kecepatan = kecepatan
  
  def maju(self):
    print("Maju dengan kecepatan",self.kecepatan, "km")

  def klakson(self):
    print("kalkson")
  
  def belok(self, arah):
    print("Belok arah", arah)


mobil1 = mobil("Avanza", 4, 60);

mobil1.maju()
mobil1.klakson()
mobil1.belok("kiri")