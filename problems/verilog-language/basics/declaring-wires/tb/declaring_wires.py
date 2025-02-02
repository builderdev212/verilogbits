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
        self.c = self.dut.c
        self.d = self.dut.d

        self.out = self.dut.out
        self.out_n = self.dut.out_n

    def zero_signals(self):
        self.a.value = 0
        self.b.value = 0
        self.c.value = 0
        self.d.value = 0

    async def set_input_val(self, val):
        self.a.value = val[0]
        self.b.value = val[1]
        self.c.value = val[2]
        self.d.value = val[3]
        await Timer(1, units="ns")

    async def logic_check(self):
        await Timer(1, units="ns")
        if (
            (bool(self.a.value) and bool(self.b.value))
            or (bool(self.c.value) and bool(self.d.value))
        ) != bool(self.out):
            raise DataError(
                f"out should be (a && b) || (c && d), but ({self.a.value} && {self.b.value}) || ({self.c.value} && {self.d.value})"
            )
        if int(self.out.value) == int(self.out_n.value):
            raise DataError(
                f"out_n should be inverse of out, but {self.out.value} == {self.out_n.value}."
            )
