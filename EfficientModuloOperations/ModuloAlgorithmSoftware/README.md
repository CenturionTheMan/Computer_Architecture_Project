# Code README

This code performs modulo computation on big numbers using a fast algorithm. It includes several utility functions to convert decimal numbers to binary arrays and vice versa, split bit arrays into subvectors, extend binary arrays with zeros, and save results in files.

Functions:

- `tens_to_bin(num)`: Converts a decimal number to a binary array.
- `bin_to_tens(bits_arr)`: Converts a binary array to a decimal number.
- `split_bit_array_into_subvectors(bits_array, subvectors_amount)`: Splits a bit array into subvectors.
- `extend_bin_with_zeros(bits_arr, zeros_amount)`: Extends a binary array with zeros by adding zeros to the beginning.
- `calculate_s(bits_arr, p, r, k)`: Calculates the 's' value based on the binary array, modulus, number of bits in a subvector, and number of subvectors.
- `modulo_computation_algorithm(x, p)`: Performs fast modulo computation on big numbers using the algorithm described in the code. Returns the computed modulo and the number of iterations performed.
- `save_in_file(x, p, counter)`: Saves the results (x, p, and counter) in a file.
- `save_in_file_with_name(x, p, counter, file_name)`: Saves the results (x, p, and counter) in a file with a specific name.
- `perform_calculations(x_max, x_min, x_step, p_max, p_min, p_step)`: Performs calculations for a range of values (x and p) and saves the results in files. It also keeps track of the maximum number of iterations performed and updates a separate file with the maximum iterations encountered.

Usage:

The entry point of the program is the `__main__` section. It demonstrates an example usage of the `modulo_computation_algorithm` function with predefined values of `x` and `p`. It prints the result of the modulo computation and the number of iterations performed.

The `perform_calculations` function will iterate over the specified range, compute the modulo using the fast algorithm, and save the results in files. It will also track the maximum number of iterations and update a separate file with the maximum iterations encountered.

Please note that this code assumes the existence of a directory named "Data/" in the current working directory where it can save the result files.
