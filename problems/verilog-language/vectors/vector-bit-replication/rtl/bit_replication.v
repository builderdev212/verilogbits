`resetall
`timescale 1ns / 1ps
`default_nettype none

module bit_replication (
    input  wire [7:0] i,
    output wire [31:0] o
);

    assign o = {{24{i[7]}}, i};

endmodule
