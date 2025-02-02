`resetall
`timescale 1ns / 1ps
`default_nettype none

module not_gate (
    input  wire i,
    output wire o
);

	assign o = !i;

endmodule