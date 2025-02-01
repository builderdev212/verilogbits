`resetall
`timescale 1ns / 1ps
`default_nettype none

module simple_wire (
    input  wire in,
    output wire out
);

    assign out = in;

endmodule