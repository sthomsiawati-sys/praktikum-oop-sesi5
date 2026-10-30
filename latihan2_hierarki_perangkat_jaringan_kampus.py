"""Latihan Praktikum 2: Hierarki Perangkat Jaringan Kampus (Inheritance)."""

class NetworkDevice:
    """Parent class untuk semua perangkat jaringan."""

    def __init__(self, device_id: str, brand: str, ip_address: str):
        self.device_id = device_id
        self.brand = brand
        self.ip_address = ip_address

    def get_status(self) -> str:
        return (f"[PERANGKAT] ID: {self.device_id} | Merek: {self.brand} | "
                f"IP: {self.ip_address}")

class RouterNode(NetworkDevice):
    """Child class: router dengan ukuran tabel routing."""

    def __init__(self, device_id: str, brand: str, ip_address: str,
                 routing_table_size: int):
        super().__init__(device_id, brand, ip_address)
        self.routing_table_size = routing_table_size

    def get_status(self) -> str:
        base_info = super().get_status()
        return (f"[ROUTER] {base_info} | "
                f"Ukuran Tabel Routing: {self.routing_table_size} entri")

class SwitchNode(NetworkDevice):
    """Child class: switch dengan jumlah port dan VLAN."""

    def __init__(self, device_id: str, brand: str, ip_address: str,
                 total_ports: int, vlan_count: int):
        super().__init__(device_id, brand, ip_address)
        self.total_ports = total_ports
        self.vlan_count = vlan_count

    def get_status(self) -> str:
        base_info = super().get_status()
        return (f"[SWITCH] {base_info} | Total Port: {self.total_ports} | "
                f"Jumlah VLAN: {self.vlan_count}")

def main():
    print("=== PENGUJIAN HIERARKI PERANGKAT JARINGAN ===")
    perangkat = NetworkDevice("NET-000", "Generic", "192.168.0.1")
    router = RouterNode("RTR-001", "Cisco", "192.168.1.1", 1500)
    switch = SwitchNode("SW-001", "Mikrotik", "192.168.1.2", 24, 8)

    print(perangkat.get_status())
    print(router.get_status())
    print(switch.get_status())

    print("\n[VERIFIKASI HIERARKI]")
    print("router instance dari NetworkDevice?",
          isinstance(router, NetworkDevice))
    print("switch instance dari NetworkDevice?",
          isinstance(switch, NetworkDevice))
    print("RouterNode subclass dari NetworkDevice?",
          issubclass(RouterNode, NetworkDevice))
    print("SwitchNode subclass dari NetworkDevice?",
          issubclass(SwitchNode, NetworkDevice))
    print("router instance dari SwitchNode?", isinstance(router, SwitchNode))
    print("MRO RouterNode:", [c.__name__ for c in RouterNode.__mro__])

if __name__ == "__main__":
    main()