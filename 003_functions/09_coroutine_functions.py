# ### 9. **Coroutine Functions (async/await)**
import asyncio

async def check_device_status(device):
    """Async function to check device status"""
    print(f"Checking {device} status...")
    await asyncio.sleep(5)  # Simulate network delay
    print(f"{device} status: OK")
    return True

async def monitor_network():
    """Monitor multiple network devices"""
    devices = ['router1', 'switch1', 'firewall1']
    tasks = [check_device_status(device) for device in devices]
    await asyncio.gather(*tasks)

# Run the async functions
asyncio.run(monitor_network())