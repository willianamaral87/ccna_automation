### 8. **Class Methods**
class NetworkDevice:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def ping(self, target):
        """Instance method to ping from this device"""
        print(f"Pinging {target} from {self.hostname} ({self.ip})")
        return True

    @classmethod
    def from_csv(cls, csv_string):
        """Alternative constructor from CSV"""
        hostname, ip = csv_string.split(',')
        return cls(hostname, ip)

    @staticmethod
    def validate_ip(ip):
        """Static method to validate IP"""
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(p) <= 255 for p in parts)

# Usage
device1 = NetworkDevice('router1', '192.168.1.1')
device1.ping('8.8.8.8')
print(device1.hostname, device1.ip)

device2 = NetworkDevice.from_csv('switch1,10.0.0.1')
print(device2.hostname, device2.ip)

print(NetworkDevice.validate_ip('256.0.0.1'))
