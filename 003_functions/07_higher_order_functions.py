### 7. **Higher-order Functions**
def log_operation(operation):
    """Decorator to log network operations"""
    def wrapper(*args, **kwargs):
        print(f"Executing {operation.__name__} on {args[0]}")
        return operation(*args, **kwargs)
    return wrapper

@log_operation
def backup_config(device):
    print(f"Backing up config for {device}")
    return True

backup_config('switch1')
