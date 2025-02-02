import logging
from cocotb.clock import Timer


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

        # Zero out signals
        self.zero_signals()

    def get_signals(self):
        self.i = self.dut.i
        self.o = self.dut.o

    def zero_signals(self):
        self.i.value = 0

    async def set_input_val(self, val):
        self.i.value = val
        await Timer(1, units="ns")

    async def is_inverse_check(self):
        await Timer(1, units="ns")
        if int(self.i.value) == int(self.o.value):
            raise DataError(
                f"Output should be inverse, but {self.i.value} == {self.o.value}."
            )
