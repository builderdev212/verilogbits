`resetall
`timescale 1ns / 1ps
`default_nettype none

module not_gate (
    input  wire in,
    output wire out
);

	assign out = !in;

endmodule