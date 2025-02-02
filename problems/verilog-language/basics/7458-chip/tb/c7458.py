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
        self.p1a = self.dut.p1a
        self.p1b = self.dut.p1b
        self.p1c = self.dut.p1c
        self.p1d = self.dut.p1d
        self.p1e = self.dut.p1e
        self.p1f = self.dut.p1f
        self.p1y = self.dut.p1y

        self.p2a = self.dut.p2a
        self.p2b = self.dut.p2b
        self.p2c = self.dut.p2c
        self.p2d = self.dut.p2d
        self.p2y = self.dut.p2y

    def zero_signals(self):
        self.p1a.value = 0
        self.p1b.value = 0
        self.p1c.value = 0
        self.p1d.value = 0
        self.p1e.value = 0
        self.p1f.value = 0

        self.p2a.value = 0
        self.p2b.value = 0
        self.p2c.value = 0
        self.p2d.value = 0

    async def set_p1_input_val(self, val):
        self.p1a.value = val[0]
        self.p1b.value = val[1]
        self.p1c.value = val[2]
        self.p1d.value = val[3]
        self.p1e.value = val[4]
        self.p1f.value = val[5]
        await Timer(1, units="ns")

    async def p1_logic_check(self):
        await Timer(1, units="ns")
        if (
            (bool(self.p1a.value) and bool(self.p1b.value) and bool(self.p1c.value))
            or (bool(self.p1d.value) and bool(self.p1e.value) and bool(self.p1f.value))
        ) != bool(self.p1y.value):
            raise DataError(
                f"(p1a && p1b && p1c) || (p1d && p1e && p1f) should be p1y, but ({self.p1a.value} && {self.p1b.value} && {self.p1c.value}) || ({self.p1d.value} && {self.p1e.value} && {self.p1f.value}) != {self.p1y.value}."
            )

    async def set_p2_input_val(self, val):
        self.p2a.value = val[0]
        self.p2b.value = val[1]
        self.p2c.value = val[2]
        self.p2d.value = val[3]
        await Timer(1, units="ns")

    async def p2_logic_check(self):
        await Timer(1, units="ns")
        if (
            (bool(self.p2a.value) and bool(self.p2b.value))
            or (bool(self.p2d.value) and bool(self.p2e.value))
        ) != bool(self.p2y.value):
            raise DataError(
                f"(p2a && p2b) || (p2c && p2d) should be p2y, but ({self.p2a.value} && {self.p2b.value}) || ({self.p2c.value} && {self.p2d.value}) != {self.p2y.value}."
            )
