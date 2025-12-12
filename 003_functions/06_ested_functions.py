### 6. **Nested Functions**
def configure_vlan(device_ip):
    """Outer function for VLAN configuration"""

    def connect_to_device():
        """Nested function to connect to device"""
        print(f"Connecting to {device_ip}...")
        return True

    def apply_config(vlan_id, name):
        """Nested function to apply config"""
        print(f"Configuring VLAN {vlan_id} ({name})")

    if connect_to_device():
        apply_config(10, 'MANAGEMENT')
        apply_config(20, 'VOICE')
        apply_config(30, 'DATA')

configure_vlan('192.168.1.1')
