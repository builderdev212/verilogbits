import os
import pytest

import cocotb
from cocotb.regression import TestFactory
from cocotb_test.simulator import run

from c7458 import TB


async def p1_logic_check(dut):
    tb = TB(dut)

    test_vals = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]

    tb.log.info("Checking output value...")

    for i in range(len(test_vals)):
        tb.set_p1_input_val(test_vals[i])
        tb.p1_logic_check()


async def p2_logic_check(dut):
    tb = TB(dut)

    test_vals = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
    ]

    tb.log.info("Checking output value...")

    for i in range(len(test_vals)):
        tb.set_p2_input_val(test_vals[i])
        tb.p2_logic_check()


if cocotb.SIM_NAME:
    test1 = TestFactory(p1_logic_check)
    test1.generate_tests()
    test2 = TestFactory(p2_logic_check)
    test2.generate_tests()

# cocotb-test

tests_dir = os.path.abspath(os.path.dirname(__file__))
rtl_dir = os.path.abspath(os.path.join(tests_dir, "..", "rtl"))

parameter_list = [{}]


@pytest.mark.parametrize("parameters", parameter_list)
def test_constant_zero(request, parameters):
    dut = "c7458"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = dut

    verilog_sources = [
        os.path.join(rtl_dir, f"{dut}.v"),
    ]

    extra_env = {f"PARAM_{k}": str(v) for k, v in parameters.items()}

    sim_build = os.path.join(
        tests_dir, "sim_build", request.node.name.replace("[", "-").replace("]", "")
    )

    run(
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        sim_build=sim_build,
        extra_env=extra_env,
        compile_args=["--timing", "-O3"],
        waves=True,
    )
