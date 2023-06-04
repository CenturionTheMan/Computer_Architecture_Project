
module sub_S_calculation(
                        input [64:1] S_in,
                        output [64:1] S_out);
    
    assign S_out =  S_in[8:1  ] * 1 +       // 2^0 = 1
                    S_in[16:9 ] * 127 +     //2^[8]mod129 = 127 (0111 1111)
                    S_in[24:17] * 4 +       //2^16(mod129) = 4
                    S_in[32:25] * 121 +     //2^24(mod129) = 121
                    S_in[40:33] * 16 +      //2^32(mod129) = 16
                    S_in[48:41] * 97 +      //2^40(mod129) = 97
                    S_in[56:49] * 64 +      //2^48(mod129) = 64
                    S_in[64:57] * 1;        //2^56(mod129) = 1
    
endmodule //sub_S_calculation


module x_modulo_129 #(parameter N = 8) 
(
    input [64:1] X,
    output [8:1] S
);

    wire [0 : N] [64:1] S_tmp;
    reg [64:1] Sfin_tmp;


    genvar i;
    
    assign S_tmp[0] = X;
    
    generate
        for (i = 0; i < N; i = i + 1) begin
            sub_S_calculation s_sub(S_tmp[i], S_tmp[i+1]);
        end
    endgenerate
    
    
    always @(S_tmp[N-1]) begin
        if (S_tmp[N-1] >= 129)
            Sfin_tmp <= S_tmp[N-1] - 129;
        else
            Sfin_tmp <= S_tmp[N-1];
    end
    
    assign S = Sfin_tmp;
    
    // Display S_tmp values in the console
    integer j;
    always @(Sfin_tmp) begin
        for (j = 0; j < N; j = j + 1) begin
            $display("S_tmp[%2d] = %d", j + 1, S_tmp[j]);
        end
        $display("S_tmp_fin = %d", Sfin_tmp);
    end
    
endmodule // x_modulo_129

module Main;
    reg [64:1] x;
    wire [8:1] s;
    
    x_modulo_129 #(.N(11)) mod(.X(x), .S(s));

    
    initial begin
        // Assign values to the inputs (x's)
        x = 5132051709291; // mod val = 84
    
        // Wait for a brief period to allow simulation to run
        #10;
        
        // Display the output values
        $display("\n\n====== RESULTS ======");
        $display("Result (s): %d", s);
        
        // Finish the simulation
        $finish;
    end
endmodule //main















