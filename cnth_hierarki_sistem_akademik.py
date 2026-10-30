class Person:
  def __init__(self, code_id: str, name: str, email: str):
    self.code_id = code_id
    self.name = name
    self.email = email

  def get_info(self) -> str:
    return f"ID: {self.code_id} | Nama: {self.name} | Email: {self.email}"

class Student(Person):
  def __init__(self, code_id: str, name: str, email: str, nim: str, gpa: float):
    super().__init__(code_id, name, email)
    self.nim = nim
    self.prodi = "Teknologi Informasi"
    self.gpa = gpa

  def get_info(self) -> str:
    base_info = super().get_info()
    return f"[MAHASISWA UNTARA] {base_info} | NIM: {self.nim} | Prodi: {self.prodi} | IPK: {self.gpa}"

class Lecturer(Person):
  def __init__(self, code_id: str, name: str, email: str, nidn: str, course: str):
    super().__init__(code_id, name, email)
    self.nidn = nidn
    self.course = course

  def get_info(self) -> str:
    base_info =  super().get_info()
    return f"[DOSEN UNTARA] {base_info} | NIDN: {self.nidn} | Pengampu: {self.course}"

# Pengujian Inheritance
mhs = Student("ID-001", "Andi Wijaya", "andi@untara.ac.id", "230101001", 3.85)
dos = Lecturer("ID-102","Dr. Henra, M.Kom", "henra@untara.ac.id", "NIDN-0412", "OOP Python")

print(mhs.get_info())
print(dos.get_info())

# Cek IsIntance & IsSubClass
print("\n[VERIFIKASI HIERARKI]")
print("Apakah mhs instance dari Person?", isinstance(mhs, Person))
print("Apakah Student subclass dari Person?", issubclass(Student, Person))
