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
        self.one = self.dut.one

    async def one_check(self):
        if int(self.one.value) != 1:
            raise DataError(f"Output should always be 1, got {self.one.value} instead.")
