"""`smbus` stub for editor use."""

class SMBus:
    """SMBus stub with basic no-op I2C methods."""

    def __init__(self, bus: int):
        self.bus = bus

    def write_byte(self, i2c_addr, value):
        """Write single byte (no-op)."""

    def write_byte_data(self, i2c_addr, register, value):
        """Write byte to device (no-op)."""

    def read_byte_data(self, i2c_addr, register):
        """Read byte from device (returns 0)."""
        return 0

    def write_i2c_block_data(self, i2c_addr, register, data):
        """Write block to device (no-op)."""

    def read_i2c_block_data(self, i2c_addr, register, length):
        """Read block from device (returns zeros)."""
        return [0] * (length or 0)

    def read_byte(self, i2c_addr):
        """Read single byte (returns 0)."""
        return 0

    def close(self):
        """Close bus (no-op)."""

    def __enter__(self):
        """Enter context (returns self)."""
        return self

    def __exit__(self, exc_type, exc, tb):
        """Exit context (no-op)."""
        return False

SMBusWrapper = SMBus
