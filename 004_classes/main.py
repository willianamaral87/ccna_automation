from network_device_class import CiscoSwitch, CiscoRouter

if __name__ == "__main__":
    # Example usage for a Cisco Switch
    switch = CiscoSwitch(
        host="192.168.1.1",
        username="admin",
        password="cisco123",
        secret="enablepass"
    )
    
    if switch.connect():
        # Execute a show command
        version_output = switch.send_command("show version")
        print(version_output)
        
        # Push configuration
        config_commands = [
            "vlan 10",
            "name account_department"
        ]
        switch.send_config_commands(config_commands)
        
        switch.disconnect()

    # Example usage for a Cisco Router
    router = CiscoRouter(
        host="192.168.1.2",
        username="admin",
        password="cisco123",
        secret="enablepass"
    )
    
    if router.connect():
        # Execute a show command
        version_output = router.send_command("show version")
        print(version_output)
        
        # Push configuration
        config_commands = [
            "interface loopback 0",
            "ip address 10.10.10.10 255.255.255.255",
            "no shutdown"
        ]
        router.send_config_commands(config_commands)
        
        router.disconnect()