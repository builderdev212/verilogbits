`resetall
`timescale 1ns / 1ps
`default_nettype none

module constant_zero (
    output wire zero
);

    assign zero = 0;

endmodule