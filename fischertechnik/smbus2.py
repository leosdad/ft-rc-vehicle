"""``smbus2`` stub for editor use."""


class i2c_msg:
    """Read/write I2C messages."""

    @staticmethod
    def read(addr, length):
        """Read block."""
        return bytes([0] * (length or 0))

    @staticmethod
    def write(addr, data):
        """Write block."""
        return bytes(data)


class SMBus:
    """SMBus with I2C methods."""

    def __init__(self, bus: int):
        """Initialize bus."""
        self.bus = bus

    def read_byte(self, addr):
        """Read single byte."""
        return 0

    def write_byte(self, addr, val):
        """Write single byte."""

    def read_i2c_block_data(self, addr, register, length):
        """Read block data."""
        return [0] * (length or 0)

    def write_i2c_block_data(self, addr, register, data):
        """Write block data."""

    def close(self):
        """Close bus."""


SMBusWrapper = SMBus
