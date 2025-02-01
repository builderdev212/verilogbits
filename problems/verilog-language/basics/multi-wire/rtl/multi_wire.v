`resetall
`timescale 1ns / 1ps
`default_nettype none

module multi_wire ( 
    input  wire a,
    input  wire b,
    input  wire c,

    output wire w,
    output wire x,
    output wire y,
    output wire z
);
    
    assign {w, x, y, z} = {a, b, b, c};

endmodule