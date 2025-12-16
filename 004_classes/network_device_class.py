from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


class NetworkDevice:
    """Base class for network device connections using Netmiko"""
    
    def __init__(self, host, username, password, device_type, secret=""):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.secret = secret
        self.connection = None

    def connect(self):
        """Establishes SSH connection to the device"""
        device_params = {
            'device_type': self.device_type,
            'host': self.host,
            'username': self.username,
            'password': self.password,
            'secret': self.secret,
        }
        
        try:
            self.connection = ConnectHandler(**device_params)
            if self.secret:
                self.connection.enable()
            print(f"Successfully connected to {self.host}")
            return True
        except NetmikoTimeoutException:
            print(f"Connection timeout to {self.host}")
            return False
        except NetmikoAuthenticationException:
            print(f"Authentication failed for {self.host}")
            return False
        except Exception as e:
            print(f"Error connecting to {self.host}: {str(e)}")
            return False

    def disconnect(self):
        """Closes the SSH connection"""
        if self.connection:
            self.connection.disconnect()
            print(f"Disconnected from {self.host}")

    def send_command(self, command):
        """Sends a show command and returns output"""
        if not self.connection:
            print("Not connected to device!")
            return None
        try:
            output = self.connection.send_command(command)
            return output
        except Exception as e:
            print(f"Error executing command: {str(e)}")
            return None

class CiscoSwitch(NetworkDevice):
    """Child class for Cisco Switch-specific operations"""
    
    def __init__(self, host, username, password, secret=""):
        super().__init__(host, username, password, 'cisco_ios', secret)

    def send_config_commands(self, commands):
        """Sends configuration commands to a Cisco switch"""
        if not self.connection:
            print("Not connected to device!")
            return False
        
        if isinstance(commands, str):
            commands = [commands]
        
        try:
            output = self.connection.send_config_set(commands)
            print(f"Configuration applied successfully to {self.host}")
            return output
        except Exception as e:
            print(f"Failed to apply config: {str(e)}")
            return False

class CiscoRouter(NetworkDevice):
    """Child class for Cisco Router-specific operations"""
    
    def __init__(self, host, username, password, secret=""):
        super().__init__(host, username, password, 'cisco_ios', secret)

    def send_config_commands(self, commands):
        """Sends configuration commands to a Cisco router"""
        if not self.connection:
            print("Not connected to device!")
            return False
        
        if isinstance(commands, str):
            commands = [commands]
        
        try:
            output = self.connection.send_config_set(commands)
            print(f"Configuration applied successfully to {self.host}")
            return output
        except Exception as e:
            print(f"Failed to apply config: {str(e)}")
            return False

