import os
import pytest
import cocotb
from cocotb.clock import Timer
from cocotb.regression import TestFactory
from cocotb_test.simulator import run

from constant_zero import TB


async def output_stays_zero(dut):
    tb = TB(dut)

    tb.log.info("Checking output value...")
    # Await one nanosecond so the model can start.
    await Timer(1, units="ns")
    tb.zero_check()


if cocotb.SIM_NAME:
    test1 = TestFactory(output_stays_zero)
    test1.generate_tests()

# cocotb-test

tests_dir = os.path.abspath(os.path.dirname(__file__))
rtl_dir = os.path.abspath(os.path.join(tests_dir, "..", "rtl"))

parameter_list = [{}]


@pytest.mark.parametrize("parameters", parameter_list)
def test_constant_zero(request, parameters):
    dut = "constant_zero"
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
