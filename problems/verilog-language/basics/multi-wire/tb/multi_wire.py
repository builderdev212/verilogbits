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

        self.w = self.dut.w
        self.x = self.dut.x
        self.y = self.dut.y
        self.z = self.dut.z

    def zero_signals(self):
        self.a.value = 0
        self.b.value = 0
        self.c.value = 0

    async def set_input_vals(self, val):
        self.a.value = val[0]
        self.b.value = val[1]
        self.c.value = val[2]
        await Timer(1, units="ns")

    async def is_equal_check(self):
        await Timer(1, units="ns")
        if int(self.w.value) != int(self.a.value):
            raise DataError(
                f"w and a should be equal, but {self.w.value} != {self.a.value}."
            )

        if int(self.x.value) != int(self.b.value):
            raise DataError(
                f"x and b should be equal, but {self.x.value} != {self.b.value}."
            )

        if int(self.y.value) != int(self.b.value):
            raise DataError(
                f"y and b should be equal, but {self.y.value} != {self.b.value}."
            )

        if int(self.z.value) != int(self.c.value):
            raise DataError(
                f"z and c should be equal, but {self.z.value} != {self.c.value}."
            )