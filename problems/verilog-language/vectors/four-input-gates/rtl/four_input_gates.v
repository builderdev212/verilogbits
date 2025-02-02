`resetall
`timescale 1ns / 1ps
`default_nettype none

module four_input_gates ( 
    input  wire [3:0] i,
    output wire       out_and,
    output wire       out_or,
    output wire       out_xor
);
    
    assign out_and = & i;
    assign out_or = | i;
    assign out_xor = ^ i;

endmodule