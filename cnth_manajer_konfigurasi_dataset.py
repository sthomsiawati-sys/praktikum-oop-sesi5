class DatasetConfig:
  def __init__(self, dataset_name: str, initial_rate_limit: int):
    self.dataset_name = dataset_name # Public attribute
    self.__access_token = "UNTARA_TOKEN_99" # Private attribute
    self.__rate_limit = max(10, initial_rate_limit) # Private attribute dengan validasi awal

  @property
  def rate_limit(self) -> int:
      """Getter untuk membaca nilai rate limit private"""
      return self.__rate_limit

  @rate_limit.setter
  def rate_limit(self, new_limit: int):
      """Setter untuk memperbarui rate limit dengan validasi"""
      if new_limit >= 10:
          self.__rate_limit = new_limit
          print(f"[SUCCESS] Rate limit diperbarui menjadi: {self.__rate_limit} req/min")
      else:
         print("[ERROR] Rate limit minimal adalah 10 req/min!")

  def get_masked_token(self) -> str:
      """Metode kontrol akses untuk menampilkan Token tersamar"""
      return f"{self.__access_token[:3]}****{self.__access_token[-2:]}"

# Uji Coba Encapsulation
config = DatasetConfig("UNTARA BigData Traffic", 100)
print(f"Dataset Name: {config.dataset_name}")
print(f"Masked Token: {config.get_masked_token()}")
print(f"Rate Limit (via @property): {config.rate_limit}")

config.rate_limit = 250
config.rate_limit = 5 # Mengetes validasi

# Coba akses langsung atribut private
try:
  print(config.__access_token)
except AttributeError as e:
   print(f"\n[AKSES DITOLAK] Akses langsung ke atribut private gagal: {e}")
  
