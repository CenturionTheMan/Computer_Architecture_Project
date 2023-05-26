module sub_S_calculation(S_out, S_in);
    output [64:1] S_out;
    input [64:1] S_in;
    
    assign S_out =  S_in[8:1  ] +                  // 2^0 = 2
                    S_in[17:9 ] * 8'b01111111 +    //2^[8]mod129 = 127 (0111 1111)
                    S_in[26:18] * 3'b100 +         //2^16(mod129) = 4
                    S_in[32:27] * 8'b01111001 +    //2^24(mod129) = 121
                    S_in[41:33] * 5'b10000 +       //2^32(mod129) = 16
                    S_in[50:42] * 7'b1100001 +     //2^40(mod129) = 97
                    S_in[59:51] * 7'b1000000 +     //2^48(mod129) = 64
                    S_in[64:60] * 1'b1;            //2^56(mod129) = 1
    
endmodule //sub_S_calculation


module x_modulo_129(S, X);
    output [8:1] S; //129 bin len is 8 (1000 0001)b
    input [64:1] X; //max X have 64 bits
    wire [64:1] S1_tmp, S2_tmp, S3_tmp, S4_tmp, S5_tmp, 
                S6_tmp, S7_tmp, S8_tmp, S9_tmp, S10_tmp;
    reg [64:1] S_tmp;
    
    
    sub_S_calculation s1(S1_tmp, X);
    sub_S_calculation s2(S2_tmp, S1_tmp);
    sub_S_calculation s3(S3_tmp, S2_tmp);
    sub_S_calculation s4(S4_tmp, S3_tmp);
    sub_S_calculation s5(S5_tmp, S4_tmp);
    sub_S_calculation s6(S6_tmp, S5_tmp);
    sub_S_calculation s7(S7_tmp, S6_tmp);
    sub_S_calculation s8(S8_tmp, S7_tmp);
    sub_S_calculation s9(S9_tmp, S8_tmp);
    sub_S_calculation s10(S10_tmp, S9_tmp);
    
                    
    always @(S10_tmp) begin
        if (S10_tmp >= 8'b10000001)
            S_tmp <= S10_tmp - 8'b10000001;
        else
            S_tmp <= S10_tmp;
    end
    
    assign S = S_tmp;
    
endmodule //x_modulo_129

module Main;
    reg [64:1] X;
    wire [8:1] Result;
    x_modulo_129 mod(Result, X);
    
    initial begin
        // Assign values to the input X
        X = 32'b11001100; // Example value
    
        // Wait for a brief period to allow simulation to run
        #10;
    
        // Display the output value
        $display("S: %d", Result);
    
        // Finish the simulation
        $finish;
    end
endmodule //main















