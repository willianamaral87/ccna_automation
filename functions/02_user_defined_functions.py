def get_device_info(hostname, ip, platform='cisco_ios'):
    """Returns a dictionary with device information"""
    return {
        'hostname': hostname,
        'ip address': ip,
        'platform': platform,
        'status': 'active'
    }

router = get_device_info('core-switch', '10.10.10.254')
print(router)

router_xr = get_device_info('core-switch', '10.10.10.10', 'cisco_xr')
print(router_xr)