`resetall
`timescale 1ns / 1ps
`default_nettype none

module reverse #(
    parameter VECTOR_SIZE = 8
)( 
    input  wire [VECTOR_SIZE-1:0] i,
    output wire [VECTOR_SIZE-1:0] o
);
    
    genvar i;
    generate
        for (i = 0; i < VECTOR_SIZE; i++) begin : INPUT_REVERSE
            assign out[VECTOR_SIZE-1-i] = in[i];
        end
    endgenerate

endmodule
