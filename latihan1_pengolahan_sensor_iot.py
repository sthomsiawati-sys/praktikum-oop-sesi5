"""Latihan Praktikum 1: Pengolahan Sensor IoT (Encapsulation)."""

class SensorDataNode:
    """Node sensor IoT kampus dengan suhu dan kelembapan terenkapsulasi."""

    TEMP_MIN = -10.0
    TEMP_MAX = 60.0

    def __init__(self, node_id: str, location: str,
                 temperature: float = 25.0, humidity: float = 50.0):
        self.node_id = node_id            # Public
        self.location = location          # Public
        self.__temperature = 25.0         # Private (nilai awal aman)
        self.__humidity = 50.0            # Private
        # Gunakan setter agar nilai awal juga divalidasi
        self.temperature = temperature
        self.humidity = humidity

    @property
    def temperature(self) -> float:
        """Getter suhu (derajat Celsius)."""
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temp: float):
        """Setter suhu dengan validasi rentang -10.0 s.d. 60.0 C."""
        if self.TEMP_MIN <= new_temp <= self.TEMP_MAX:
            self.__temperature = float(new_temp)
            print(f"[SUCCESS] Suhu {self.node_id} diperbarui: "
                  f"{self.__temperature} C")
        else:
            print(f"[ERROR] Suhu {new_temp} C ditolak! Rentang valid: "
                  f"{self.TEMP_MIN} s.d. {self.TEMP_MAX} C")

    @property
    def humidity(self) -> float:
        """Getter kelembapan (persen)."""
        return self.__humidity

    @humidity.setter
    def humidity(self, new_humidity: float):
        """Setter kelembapan dengan validasi 0 - 100 persen."""
        if 0.0 <= new_humidity <= 100.0:
            self.__humidity = float(new_humidity)
        else:
            print(f"[ERROR] Kelembapan {new_humidity}% ditolak! "
                  f"Rentang valid: 0 s.d. 100%")

    def get_status_summary(self) -> str:
        """Mengembalikan ringkasan telemetry sensor."""
        return (f"[SENSOR {self.node_id}] Lokasi: {self.location} | "
                f"Suhu: {self.__temperature:.1f} C | "
                f"Kelembapan: {self.__humidity:.1f}%")

def main():
    print("=== PENGUJIAN SensorDataNode ===")
    node = SensorDataNode("IOT-001", "Lab Komputer UNTARA", 28.5, 65.0)
    print(node.get_status_summary())

    print("\n--- Uji suhu valid ---")
    node.temperature = 35.0
    node.temperature = -10.0   # batas bawah
    node.temperature = 60.0    # batas atas

    print("\n--- Uji suhu di luar rentang (harus ditolak) ---")
    node.temperature = 75.0
    node.temperature = -25.5
    print(f"Suhu setelah uji penolakan: {node.temperature} C")

    print("\n--- Uji akses langsung atribut private ---")
    try:
        print(node.__temperature)
    except AttributeError as e:
        print(f"[AKSES DITOLAK] {e}")

    print("\n--- Verifikasi dengan assert ---")
    node.temperature = 30.0
    node.temperature = 100.0
    assert node.temperature == 30.0, "Suhu invalid seharusnya ditolak"
    print("[LULUS] Suhu di luar rentang berhasil ditolak.")

    print("\n" + node.get_status_summary())

if __name__ == "__main__":
    main()
    