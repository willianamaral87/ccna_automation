from pytest_vlan_validator import VlanValidator

def main():
    validator = VlanValidator()

    vlan = int(input("Enter a VLAN number: "))

    if validator.is_valid_vlan(vlan):
        print("VLAN is VALID ✅")
    else:
        print("VLAN is INVALID ❌")

if __name__ == "__main__":
    main()