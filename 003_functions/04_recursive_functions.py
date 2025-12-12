### 4. **Recursive Functions**
def count_down(device, seconds):
    """Recursive countdown for device reboot"""
    if seconds <= 0:
        print(f"{device} rebooted!")
    else:
        print(f"{device} rebooting in {seconds} seconds...")
        count_down(device, seconds - 1)

count_down('core-router', 5)
