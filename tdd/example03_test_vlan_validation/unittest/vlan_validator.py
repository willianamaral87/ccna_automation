class VlanValidator:

    def is_valid_vlan(self, vlan):
        if not isinstance(vlan, int):
            return False
        if vlan < 1 or vlan > 4094:
            return False
        return True