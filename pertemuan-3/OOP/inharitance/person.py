class person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)


class Student(person):
  def __init__(self,fname, lname,year):
    super().__init__(fname, lname)
    self.graduation = year
  
  def welcome(self):
    print("Selamat datang", self.firstname, self.lastname, "Di kampus Sekolah Tinggi Terpadu nurul fikri tahun",self.graduation)
  

x = Student("Muhamad","Zaki",2021)
x.welcome()