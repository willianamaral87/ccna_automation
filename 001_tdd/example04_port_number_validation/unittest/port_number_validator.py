class PortNumberValidator:

    def is_valid_port(self, port):
        if not isinstance(port, int):
            return False
        if port < 1 or port > 65535:
            return False
        return True