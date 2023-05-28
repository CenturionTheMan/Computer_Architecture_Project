module sub_S_calculation(S_out, S_in);
    output [64:1] S_out;
    input [64:1] S_in;
    
    assign S_out =  S_in[8:1  ] * 1 +                  // 2^0 = 1
                    S_in[16:9 ] * 127 +    //2^[8]mod129 = 127 (0111 1111)
                    S_in[24:17] * 4 +         //2^16(mod129) = 4
                    S_in[32:25] * 121 +    //2^24(mod129) = 121
                    S_in[40:33] * 16 +       //2^32(mod129) = 16
                    S_in[48:41] * 97 +     //2^40(mod129) = 97
                    S_in[56:49] * 64 +     //2^48(mod129) = 64
                    S_in[64:57] * 1;            //2^56(mod129) = 1
    
endmodule //sub_S_calculation


module x_modulo_129(S, X);
    output [8:1] S; //129 bin len is 8 (1000 0001)b
    input [64:1] X; //max X have 64 bits
    wire [64:1] S1_tmp, S2_tmp, S3_tmp, S4_tmp, S5_tmp, 
                S6_tmp, S7_tmp, S8_tmp, S9_tmp, S10_tmp, Sfin_tmp;
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
    sub_S_calculation s11(Sfin_tmp, S10_tmp);
    
    always @(Sfin_tmp) begin
        $display("x  : %d", X);
        $display("s1 : %d", S1_tmp);
        $display("s2 : %d", S2_tmp);
        $display("s3 : %d", S3_tmp);
        $display("s4 : %d", S4_tmp);
        $display("s5 : %d", S5_tmp);
        $display("s6 : %d", S6_tmp);
        $display("s7 : %d", S7_tmp);
        $display("s8 : %d", S8_tmp);
        $display("s9 : %d", S9_tmp);
        $display("s10: %d", S10_tmp);
        $display("s11: %d\n", Sfin_tmp);
    end
                    
    always @(Sfin_tmp) begin
        if (Sfin_tmp >= 129)
            S_tmp <= Sfin_tmp - 129;
        else
            S_tmp <= Sfin_tmp;
    end
    
    assign S = S_tmp;
    
endmodule //x_modulo_129

module Main;
    reg [64:1] x1, x2, x3, x4, x5, x6;
    wire [8:1] s1, s2, s3, s4, s5, s6;
    
    x_modulo_129 mod1(s1, x1);
    x_modulo_129 mod2(s2, x2);
    x_modulo_129 mod3(s3, x3);
    x_modulo_129 mod4(s4, x4);
    x_modulo_129 mod5(s5, x5);
    x_modulo_129 mod6(s6, x6);
    
    initial begin
        // Assign values to the inputs (x's)
        
        x1 = 2721979;       // mod val = 79
        x2 = 623541;        // mod val = 84
        x3 = 98162;         // mod val = 122
        x4 = 41290864012;   // mod val = 19
        x5 = 41240719287;   // mod val = 45
        x6 = 5132051709291; // mod val = 84
    
        // Wait for a brief period to allow simulation to run
        #10;
        
        // Display the output values
        $display("\n\n====== RESULTS ======");
        $display("Result 1 (s1): %d", s1);
        $display("Result 2 (s2): %d", s2);
        $display("Result 3 (s3): %d", s3);
        $display("Result 4 (s4): %d", s4);
        $display("Result 5 (s5): %d", s5);
        $display("Result 6 (s6): %d", s6);
        
        // Finish the simulation
        $finish;
    end
endmodule //main















