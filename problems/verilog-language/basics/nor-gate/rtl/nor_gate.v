`resetall
`timescale 1ns / 1ps
`default_nettype none

module nor_gate ( 
    input  wire a,
    input  wire b, 
    output wire out
);

    assign out = !(a || b);
    
endmodule