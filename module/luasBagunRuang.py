import math
# module hitung luas baguan ruang 

def luasKubus(sisi):
  luas = 6 * sisi * sisi
  print("Luas kubus = ", luas)

def luasBalok(t, p, l):
  luasBalok = 2 * (p*l + p*t + l*t)
  print("Tinggi = ", t)
  print("panjang = ", p)
  print("lebar = ", l)
  print("Jadi luas permukaan bangun ruang luasBalok adalah ", luasBalok)


def luasTabung(jari2, t):
  phi = 3.14
  LuasTabung = 2 * phi * jari2 * (jari2 + t)
  print(math.ceil(LuasTabung))


def luasKerucut(r, s):
  phi = 22/7
  luasAlas = phi * r**2
  luasSelimut = phi * r * s
  luasPermukaan = luasAlas + luasSelimut

  print(luasPermukaan)


def luasLimas(luasAlas, jumlahSisiTegak):
    luas = luasAlas + jumlahSisiTegak

    print("Luas Limas adalah", luas)