`resetall
`timescale 1ns / 1ps
`default_nettype none

module vector_gates ( 
    input  wire [2:0] a,
    input  wire [2:0] b,
    output wire [2:0] out_or_bitwise,
    output wire       out_or_logical,
    output wire [5:0] out_not
);
    
    assign out_or_bitwise = a | b;
    assign out_or_logical = a || b;
    assign out_not = {~b, ~a};

endmodule