class bank:
  norek = ''
  nasabah = ''
  saldo = ''

  def __init__(self, norek, nasabah, saldo):
    self.norek = norek
    self.nasabah = nasabah
    self.saldo = saldo
  
  def nabung(self, uang):
    self.saldo += uang
  
  def tarik(self, uang):
    self.saldo -= uang

  def cetak(self):
    print('\n==========================',
'\nNo.Rekening\t:',self.norek,
'\nNama Nasabah\t:',self.nasabah,
'\nSaldo\t\t: Rp. ',format(self.saldo,','),
'\n--------------------------'
)


zaki = bank('09929919', "Zaki", 300000)
Rafi = bank('09929918', "rafi", 800000)

zaki.nabung(100000)


zaki.cetak()
Rafi.nabung(4000000)
Rafi.cetak()