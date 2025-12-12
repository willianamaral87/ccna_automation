### 5. **Generator Functions**
def interface_generator(prefix, count):
    """Generates interface names"""
    for i in range(1, count + 1):
        yield f"{prefix}{i}"

# Create 5 Gigabit interfaces
for interface in interface_generator('Gi0/', 5):
    print(f"Configuring {interface}...")
