# ### 10. **Partial Functions**
from functools import partial

def configure_interface(device, interface, config):
    print(f"Configuring {interface} on {device}: {config}")

# Create specialized functions
configure_gig0_1 = partial(configure_interface, 'router1', 'Gig0/1')
configure_gig0_2 = partial(configure_interface, 'router1', 'Gig0/2')

# Use the partial functions
configure_gig0_1("description UPLINK_TO_CORE")
configure_gig0_2("access vlan 10")
