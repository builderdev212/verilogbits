`resetall
`timescale 1ns / 1ps
`default_nettype none

module top_module (
    input  wire        a,
    input  wire        b,
    input  wire        c,
    input  wire        d,
    input  wire        e,
    output wire [24:0] out
);

    assign out = ~{{5{a}}, {5{b}}, {5{c}}, {5{d}}, {5{e}}} ^ {5{a, b, c, d, e}};

endmodule