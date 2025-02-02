`resetall
`timescale 1ns / 1ps
`default_nettype none

module vector_splitter ( 
    input  wire [15:0] i,
    output wire [7:0]  out_hi,
    output wire [7:0]  out_lo
);
    
    assign out_hi = i[15:8];
    assign out_lo = i[7:0];

endmodule