class Animal():
  def __init__(self,name, makanan, hidup, berkembang_biak ):
    self.name = name
    self.makanan = makanan
    self.hidup = hidup
    self.berkembang_biak = berkembang_biak

class Kucing(Animal):
  def __init__(self,name,makanan, hidup, berkembang_biak, berkaki):
    super().__init__(name,makanan, hidup, berkembang_biak) 
    self.berkaki = berkaki
  
  def suaraKucing(self):
    return "meow meow"
  
  def cetak(self):
    print("Nama Hewan :", self.name)
    print("Makanan :", self.makanan)
    print("Hidup di :", self.hidup)
    print("Berkembang biak :", self.berkembang_biak)
    print("Suara Kucing :", self.suaraKucing())
    print("Berkaki :", self.berkaki)

a = Kucing()
a.cetak()
