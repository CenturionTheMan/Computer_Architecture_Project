import math
import os
import time
from ModuloAlgorithm import modulo_computation_algorithm
from ModularProductAlgorithm import calculate_modular_product


# Function to save results in a file
def save_in_file(x, p, counter):
    directory_path = "Data/"
    f = open(directory_path + f'mod_{p}.csv', "a")
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
    directory_path = "Data/"
    max_file_path = "current_max_255.csv"
    if os.path.exists(directory_path + max_file_path):
        f = open(max_file_path, "r")
        content = f.read()
        lines = content.split("\n")
        lines.pop()
        val_str = lines.pop().split(";")[2]
        max_iterations = int(val_str)

    for p in range(p_min, p_max + 1, p_step):
        if os.path.exists(directory_path + f'mod_{p}.csv'):
            os.remove(directory_path + f'mod_{p}.csv')
        start = time.time()
        for x in range(x_min, x_max + 1, x_step):
            if x % (x_step * 100) == 0:
                print(f'p = {p} | x = {x} | perc = {(x*100/x_max):0.15f}%')
            x_mod_p, counter = modulo_computation_algorithm(x, p)
            save_in_file(x, p, counter)
            if counter > max_iterations:
                max_iterations = counter
                save_in_file_with_name(x,p,counter,directory_path + max_file_path)
            if x_mod_p != x % p:
                print("ERROR!")
        end = time.time()
        minutes = int(math.floor((end-start)/60))
        seconds = int(end - start - minutes*60)
        print(f'Done for mod{p} in {minutes} min {seconds} sec\n')


# Entry point of the program
if __name__ == '__main__':
    a = 45
    b = 15
    p = 47
    res = calculate_modular_product(a, b, p)
    print(f"{a}*{b}(mod{p}) = {a * b % p}")
    print(f"algh res = {res}")

    #x = 2721979
    #p = 129
    #res, iterations = modulo_computation_algorithm(x, p)

    #print("\nRESULT:")
    #print(f"{x}(mod{p}) = {x%p}")
    #print(f"Algorithm result = {res} | iterations amount = {iterations}")

    #print("BEGINS...")
    #p_min = 2
    #p_step = 16_777_217
    #p_32 = 4_294_967_295
    #x_min = 0
    #x_step = 1_000_000_000_003
    #x_64 = bin_to_tens([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    #perform_calculations(x_64, x_min, x_step, 255, 255, 1)
    #print('END')

