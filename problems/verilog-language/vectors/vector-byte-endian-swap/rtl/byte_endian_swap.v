`resetall
`timescale 1ns / 1ps
`default_nettype none

module byte_endian_swap #(
    parameter BYTE_COUNT = 4,
    parameter BYTE_SIZE = 8
)( 
    input  wire [(BYTE_COUNT*BYTE_SIZE)-1:0] i,
    output wire [(BYTE_COUNT*BYTE_SIZE)-1:0] o
);
    
    genvar i;
    generate
        for (i = 0; i < BYTE_COUNT; i++) begin : OUTPUT_ASSIGNMENT
        	assign o[(BYTE_SIZE*(BYTE_COUNT-i))-1:(BYTE_SIZE*(BYTE_COUNT-1-i))] = i[(BYTE_SIZE*(1+i))-1:BYTE_SIZE*i];
    	end
    endgenerate

endmodule