# Class to validate an IP address.
class IPValidator:
    def is_valid_ipv4(self, ip):
        # Separate an IP address into four parts divided by dots.
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            # If any octet is not a number.
            if not part.isdigit():
                return False
            # Convert string to number
            num = int(part)
            if num < 0 or num > 255:
                return False
        # Return True if the IP address is successfully validated.
        return True