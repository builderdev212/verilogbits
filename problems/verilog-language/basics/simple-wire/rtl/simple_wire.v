`resetall
`timescale 1ns / 1ps
`default_nettype none

module simple_wire (
    input  wire i,
    output wire o
);

    assign o = i;

endmodule