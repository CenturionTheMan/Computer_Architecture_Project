import math
import numpy as np
import os
import time


# Function to convert a decimal number to a binary array
def tens_to_bin(num):
    bits_arr = [int(i) for i in list('{0:0b}'.format(num))]
    return bits_arr


# Function to convert a binary array to a decimal number
def bin_to_tens(bits_arr):
    res = 0
    base = 0
    for bit in reversed(bits_arr):
        res = res + bit * pow(2, base)
        base = base + 1
    return int(res)


# Function to split a bit array into subvectors
def split_bit_array_into_subvectors(bits_array, subvectors_amount):
    result_array = np.array_split(bits_array, subvectors_amount)
    return result_array


# Function to extend a binary array with zeros (zeros are added to beginning)
def extend_bin_with_zeros(bits_arr, zeros_amount):
    zeros_to_add = []
    for i in range(zeros_amount):
        zeros_to_add.append(0)
    zeros_to_add.extend(bits_arr)
    return zeros_to_add


# Function to calculate 's' value
def calculate_s(bits_arr, p, r, k):
    s = 0
    i = 1
    for i in range(1,k+1):
        sub_X = bits_arr.pop()
        sub_x = int(bin_to_tens(sub_X))
        cons = int(pow(2, r * (i - 1))) % p
        s = s + sub_x * cons
    return int(s)


# Function to perform fast modulo computation on big numbers
def modulo_computation_algorithm(x, p):
    X = tens_to_bin(x)
    r = int(math.ceil(math.log2(p)))
    k = int(math.ceil(len(X) / r))

    if len(X) < k * r:
        X = extend_bin_with_zeros(X, k * r - len(X))

    X = split_bit_array_into_subvectors(X, k)
    s1 = calculate_s(X, p, r, k)

    s_temp = s1
    loop_counter = 1
    while s_temp >= 2 * p:
        loop_counter = loop_counter + 1
        S_temp = tens_to_bin(s_temp)
        n_temp = len(S_temp)
        k_temp = int(math.ceil(n_temp/r))
        if len(S_temp) < k_temp * r:
            S_temp = extend_bin_with_zeros(S_temp, k_temp * r - len(S_temp))
        S_temp = split_bit_array_into_subvectors(S_temp, k_temp)
        s_temp = calculate_s(bits_arr=S_temp, p=p, r=r, k=k_temp)

    if p <= s_temp:
        return s_temp - p, loop_counter
    else:
        return s_temp, loop_counter


# Function to save results in a file
def save_in_file(x, p, counter):
    f = open(f'mod_{p}.csv', "a")
    f.write(f'{x};{p};{counter}\n')
    f.close()


# Function to save results in a file with a specific name
def save_in_file_with_name(x, p, counter, file_name):
    f = open(file_name, "a")
    f.write(f'{x};{p};{counter}\n')
    f.close()


# Function to perform calculations for a range of values (will save results in files)
def perform_calculations(x_max, x_min, x_step, p_max, p_min, p_step):
    max_iterations = -1
    max_file_path = "current_max_255.csv"
    if os.path.exists(max_file_path):
        f = open(max_file_path, "r")
        content = f.read()
        lines = content.split("\n")
        lines.pop()
        val_str = lines.pop().split(";")[2]
        max_iterations = int(val_str)

    for p in range(p_min, p_max + 1, p_step):
        if os.path.exists(f'mod_{p}.csv'):
            os.remove(f'mod_{p}.csv')
        start = time.time()
        for x in range(x_min, x_max + 1, x_step):
            if x % (x_step * 100) == 0:
                print(f'p = {p} | x = {x} | perc = {(x*100/x_max):0.15f}%')
            x_mod_p, counter = modulo_computation_algorithm(x, p)
            save_in_file(x, p, counter)
            if counter > max_iterations:
                max_iterations = counter
                save_in_file_with_name(x,p,counter,max_file_path)
            if x_mod_p != x % p:
                print("ERROR!")
        end = time.time()
        minutes = int(math.floor((end-start)/60))
        seconds = int(end - start - minutes*60)
        print(f'Done for mod{p} in {minutes} min {seconds} sec\n')


# Entry point of the program
if __name__ == '__main__':
    x = 2^32-1
    p = 255
    res, iterations = modulo_computation_algorithm(x, p)

    print("\nRESULT:")
    print(f"{x}(mod{p}) = {x%p}")
    print(f"Algorithm result = {res} | iterations amount = {iterations}")

    #print("BEGINS...")
    #p_min = 2
    #p_step = 16_777_217
    #p_32 = 4_294_967_295
    #x_min = 0
    #x_step = 1_000_000_000_003
    #x_64 = bin_to_tens([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    #perform_calculations(x_64, x_min, x_step, 255, 255, 1)
    #print('END')

