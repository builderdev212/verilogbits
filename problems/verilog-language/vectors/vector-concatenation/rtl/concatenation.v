`resetall
`timescale 1ns / 1ps
`default_nettype none

module concatenation (
    input  wire [4:0] a,
    input  wire [4:0] b,
    input  wire [4:0] c,
    input  wire [4:0] d,
    input  wire [4:0] e,
    input  wire [4:0] f,

    output wire [7:0] w,
    output wire [7:0] x,
    output wire [7:0] y,
    output wire [7:0] z
);

    assign {w, x, y, z} = {a, b, c, d, e, f, 2'b11};

endmodule
