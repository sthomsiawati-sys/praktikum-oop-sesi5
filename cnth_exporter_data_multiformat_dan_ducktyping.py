class CSVExporter:
    def __init__(self, filename: str):
        self.filename = filename

    def export(self, data: list) -> str:
        return f"[CSV EXPORTER] Berhasil mengekspor {len(data)} rekam data ke '{self.filename}.csv'"

class JSONExporter:
    def __init__(self, filename: str):
        self.filename = filename

    def export(self, data: list) -> str:
        return f"[JSON EXPORTER] Berhasil memformat & menyimpan {len(data)} dokumen JSON ke '{self.filename}.json'"

class SQLExporter:
    def __init__(self, table_name: str):
        self.table_name = table_name

    def export(self, data: list) -> str:
        return f"[SQL EXPORTER] Berhasil melakukan INSERT BATCH {len(data)} baris ke tabel '{self.table_name}'"

# Fungsi Polimorfis berbasis Duck Typing
def run_data_export(exporter_object, dataset: list):
    print("=== PROSES EKSPOR DATA POLIMORFIS ===")
    result_message = exporter_object.export(dataset)
    print(result_message)

# Pengujian Duck Typing
sample_data = [{"id": 1, "val": 95}, {"id": 2, "val": 88}, {"id": 3, "val": 92}]

run_data_export(CSVExporter("laporan_analisis"), sample_data)
run_data_export(JSONExporter("stream_telemetry"), sample_data)
run_data_export(SQLExporter("tbl_bigdata_untara"), sample_data)

