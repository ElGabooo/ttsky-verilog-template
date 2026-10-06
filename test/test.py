# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Configura el reloj a 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Secuencia de Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Prueba 1: entrada todo en 0 -> ui_in = 0b00000000
    # Esperado: 4 bits superiores en 0 (0000) y 4 inferiores negados (1111) = 0b00001111 (15)
    dut.ui_in.value = 0b00000000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00001111, f"Fallo test 1: salida fue {dut.uo_out.value}"

    # Prueba 2: entrada todo en 1 -> ui_in = 0b11111111
    # Esperado: 4 bits superiores en 1 (1111) y 4 inferiores negados (0000) = 0b11110000 (240)
    dut.ui_in.value = 0b11111111
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b11110000, f"Fallo test 2: salida fue {dut.uo_out.value}"
