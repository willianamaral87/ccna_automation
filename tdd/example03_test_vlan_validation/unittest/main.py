from vlan_validator import VlanValidator

def main():
    validator = VlanValidator()

    vlan = input("Enter a VLAN number: ")

    # Convert input to int safely
    if vlan.isdigit():
        vlan = int(vlan)
    else:
        print("Invalid input. Must be a number.")
        return

    if validator.is_valid_vlan(vlan):
        print(f"VLAN {vlan} is VALID ✅")
    else:
        print(f"VLAN {vlan} is INVALID ❌")

if __name__ == "__main__":
    main()