from ip_validator import IPValidator

def main():
    validator = IPValidator()
    
    while True:
        ip = input("Enter an IPv4 address to validate (or 'exit' to quit): ")
        if ip.lower() == "exit":
            print("Exiting the validator. Goodbye!")
            break
        if validator.is_valid_ipv4(ip):
            print(f"✅ '{ip}' is a valid IPv4 address.\n")
        else:
            print(f"❌ '{ip}' is NOT a valid IPv4 address.\n")

if __name__ == "__main__":
    main()
