import logging


class DataError(Exception):
    pass


class TB:
    def __init__(self, dut):
        self.dut = dut

        # Start logging
        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        # Simulation Signals
        self.get_signals()

    def get_signals(self):
        self.zero = self.dut.zero

    async def zero_check(self):
        if int(self.zero.value) != 0:
            raise DataError(
                f"Output should always be 0, got {self.zero.value} instead."
            )
