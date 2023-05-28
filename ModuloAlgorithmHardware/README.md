# X mod 129 Hardware Implementation

This code implements a modulo computation algorithm for a specific modulus of 129. 
It includes two modules: sub_S_calculation and x_modulo_129, along with a Main module for testing.

### 'sub_S_calculation' Module
The sub_S_calculation module performs a calculation to obtain the value of S_out based on the input S_in. 
It uses specific bit slicing and multiplication operations to calculate each component of S_out.

### 'x_modulo_129' Module
The x_modulo_129 module utilizes ten instances of the sub_S_calculation module to perform a series of calculations. 
It propagates the results from one instance to the next until the final result is obtained in S10_tmp. 
It also includes a combinatorial always block to adjust the value of S_tmp based on the value of S10_tmp, 
ensuring the correct modulus value is achieved.

### 'Main Module'
The Main module serves as a testbench for the x_modulo_129 module. 
It defines a 64-bit input X and a 8-bit output Result. It initializes X with a sample value, 
waits for a brief period to allow simulation to run, and then displays the value of Result using the $display system task. 
Finally, it finishes the simulation using the $finish system task.

## Usage
To use this code, follow these steps:

Instantiate the x_modulo_129 module in your design hierarchy, providing the appropriate input and output signals.
Assign values to the X input signal in the Main module according to your requirements.
Simulate the design using a Verilog simulator.
When simulating, ensure that all the necessary modules (sub_S_calculation, x_modulo_129, and Main) are included in the simulation and properly connected.

Note: The code includes an example value for X (32'b11001100). You can modify this value to test different inputs and observe the corresponding output in Result.
