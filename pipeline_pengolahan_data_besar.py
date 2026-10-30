"""Proyek Terintegrasi: Pipeline Analisis Data Besar (Studi Kasus UNTARA).Menggabungkan Encapsulation, Inheritance, dan Polymorphism."""

from abc import ABC, abstractmethod

# 1. ENCAPSULATION & ABSTRACTION (Base Data Processor)
class BaseDataProcessor(ABC):
    def __init__(self, datasource_name: str, batch_size: int):
        self.datasource_name = datasource_name
        self.__batch_size = max(1, batch_size)  # Encapsulated attribute
        self._processed_count = 0               # Protected attribute

    @property
    def batch_size(self) -> int:
        return self.__batch_size

    @abstractmethod
    def load_data(self):
        """Metode abstrak yang wajib di-override oleh child class."""

    @abstractmethod
    def process_data(self):
        """Metode abstrak pemrosesan data."""

# 2. INHERITANCE & METHOD OVERRIDING (CSV Processor)
class CSVDataProcessor(BaseDataProcessor):
    def load_data(self):
        print(f"[CSV LOADER] Membaca file CSV '{self.datasource_name}' "
              f"dengan batch_size={self.batch_size}...")

    def process_data(self):
        self._processed_count += 5000
        print(f"[CSV PROCESSOR] Berhasil memproses "
              f"{self._processed_count} baris data CSV.")

# INHERITANCE & METHOD OVERRIDING (JSON Stream Processor)
class JSONStreamProcessor(BaseDataProcessor):
    def load_data(self):
        print(f"[JSON STREAM] Terhubung ke Stream "
              f"'{self.datasource_name}'...")

    def process_data(self):
        self._processed_count += 12000
        print(f"[JSON PROCESSOR] Berhasil memfilter & mensinkronisasi "
              f"{self._processed_count} dokumen JSON Big Data.")

# 3. POLYMORPHISM & DYNAMIC DISPATCH (Pipeline Engine)
class BigDataPipelineEngine:
    def __init__(self, pipeline_name: str):
        self.pipeline_name = pipeline_name
        self.processors = []

    def add_processor(self, processor: BaseDataProcessor):
        self.processors.append(processor)

    def execute_pipeline(self):
        print(f"\n================ MENGEKSEKUSI PIPELINE: "
              f"{self.pipeline_name} ================")
        for p in self.processors:
            p.load_data()
            p.process_data()
            print("-" * 60)

# EKSEKUSI PROYEK TERINTEGRASI
def main():
    pipeline = BigDataPipelineEngine("UNTARA Big Data Analytics Engine v1.0")
    pipeline.add_processor(CSVDataProcessor("data_telemetry_2026.csv", 1000))
    pipeline.add_processor(JSONStreamProcessor("stream_data_untara", 2500))
    pipeline.execute_pipeline()

    print("\n[UJI TAMBAHAN]")
    try:
        BaseDataProcessor("x", 10)
    except TypeError as e:
        print(f"[ABSTRACT CLASS] Tidak dapat diinstansiasi: {e}")

    cek = CSVDataProcessor("uji.csv", -5)
    print(f"batch_size dengan input -5 menjadi: {cek.batch_size}")
    try:
        cek.batch_size = 99
    except AttributeError as e:
        print(f"[READ-ONLY] batch_size tidak dapat diubah: {e}")

if __name__ == "__main__":
    main()