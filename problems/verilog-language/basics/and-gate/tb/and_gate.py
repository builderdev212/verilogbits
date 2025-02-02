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
        self.a = self.dut.a
        self.b = self.dut.b

        self.out = self.dut.out

    def zero_signals(self):
        self.a.value = 0
        self.b.value = 0

    async def set_input_val(self, val):
        self.a.value = val[0]
        self.b.value = val[1]
        await Timer(1, units="ns")

    async def logic_check(self):
        await Timer(1, units="ns")
        if (bool(self.a.value) and bool(self.b.value)) != bool(self.out.value):
            raise DataError(
                f"a && b should be output, but ({self.a.value} && {self.b.value}) != {self.out.value}."
            )
