import math
import os
import time
import matplotlib.pyplot as plt
from ModuloAlgorithm import modulo_computation_algorithm
from NumbersManipulations import *

import random
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
                print(f'p = {p} | x = {x} | perc = {(x * 100 / x_max):0.15f}%')
            x_mod_p, counter = modulo_computation_algorithm(x, p)
            save_in_file(x, p, counter)
            if counter > max_iterations:
                max_iterations = counter
                save_in_file_with_name(x, p, counter, directory_path + max_file_path)
            if x_mod_p != x % p:
                print("ERROR!")
        end = time.time()
        minutes = int(math.floor((end - start) / 60))
        seconds = int(end - start - minutes * 60)
        print(f'Done for mod{p} in {minutes} min {seconds} sec\n')


def calculate_p(p):
    punkt = 2 * p + 1
    length_of_p = len(tens_to_bin(punkt))
    return length_of_p


def find_lengths(s_temps):
    binary_lengths = []
    for s_temp in s_temps:
        length = len(tens_to_bin(s_temp))
        binary_lengths.append(length)
    return binary_lengths


def print_function(s_temps, p, name):
    s_temps_numbers = []
    s_temps_p = []

    p_length = calculate_p(p)

    for i in range(0, len(s_temps)):
        s_temps_numbers.append('s_temp' + str(i))
        s_temps_p.append(p_length)

    plt.scatter(s_temps_numbers, s_temps)
    plt.plot(s_temps_numbers, s_temps_p, color='red', label="Threshold (P_binary_length * 2 + 1)")
    plt.legend();
    plt.xlabel('Iteracja petli')
    plt.ylabel('s_temp(długość binarna)')
    plt.xticks(rotation=30, ha='right')
    plt.title(name, fontsize = 10)
    plt.grid(True)
    plt.show()


def generate_binary_number(length):
    binary_number = "1"
    for _ in range(length - 1):
        bit = random.choice([0, 1])
        binary_number += str(bit)
    return binary_number


def proportion(x_size, p_size):
    x = generate_binary_number(x_size)
    p = generate_binary_number(p_size)
    s_temp, loop_counter, s_temps = modulo_computation_algorithm(bin_to_tens(x),
                                                                 bin_to_tens(p))
    print_function(find_lengths(s_temps), bin_to_tens(p), f"Wykres dla \n"
                                                          f"x={bin_to_tens(x)} długość binarna: {len(x)}\n"
                                                          f"p={bin_to_tens(p)} długość binarna: {len(p)}")


# Entry point of the program
if __name__ == '__main__':
    a = 45
    b = 15
    p = 47
    data = []
    # calculate_p()
    s_temp, loop_counter, s_temps = modulo_computation_algorithm(6553087086, 129)
    print_function(find_lengths(s_temps), 129, f"Wykres dla \n"
                                               f"x=6 553 087 086 długość binarna: {len(tens_to_bin(6_553_087_086))}\n"
                                               f"p=129 długość binarna: {len(tens_to_bin(129))}")

    s_temp, loop_counter, s_temps = modulo_computation_algorithm(99_999_987_086, 129)
    print_function(find_lengths(s_temps), 129, f"Wykres dla\n"
                                               f"x=99 999 987 086 długość binarna: {len(tens_to_bin(99_999_987_086))}\n "
                                               f"p=129 długość binarna: {len(tens_to_bin(129))}")

    s_temp, loop_counter, s_temps = modulo_computation_algorithm(281_474_976_710, 129)
    print_function(find_lengths(s_temps), 129, f"Wykres dla \n"
                                               f"x=281 474 976 710 długość binarna: {len(tens_to_bin(281_474_976_710))} \n"
                                               f"p=129 długość binarna: {len(tens_to_bin(129))}")

    s_temp, loop_counter, s_temps = modulo_computation_algorithm(549_824_036_864, 129)
    print_function(find_lengths(s_temps), 129, f"Wykres dla \n"
                                               f"x=549 824 036 864, długość binarna: {len(tens_to_bin(549_824_036_864))}\n"
                                               f"p=129, długość binarna: {len(tens_to_bin(129))}")

    proportion(100, 10)
    proportion(90, 10)
    proportion(80, 10)
    proportion(70, 10)
    proportion(60, 10)
    proportion(50, 10)
    proportion(40, 10)
    proportion(30, 10)
    proportion(20, 10)
    proportion(10, 10)

    #
    # with open("data.csv","a") as file:
    #     for i in range(0, 2**16):
    #         for j in range(0, 2**16):
    #             res = calculate_modular_product(i, j, p)
    #             inner_data = [i, j, p, res]
    #             print(j)
    #             file.write(f"{i},{j},{p},{res}\n")
    # res =
    # print(f"{a}*{b}(mod{p}) = {a * b % p}")
    # print(f"algh res = {res}")

    # x = 2721979
    # p = 129
    # res, iterations = modulo_computation_algorithm(x, p)

    # print("\nRESULT:")
    # print(f"{x}(mod{p}) = {x%p}")
    # print(f"Algorithm result = {res} | iterations amount = {iterations}")

    # print("BEGINS...")
    # p_min = 2
    # p_step = 16_777_217
    # p_32 = 4_294_967_295
    # x_min = 0
    # x_step = 1_000_000_000_003
    # x_64 = bin_to_tens([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    # perform_calculations(x_64, x_min, x_step, 255, 255, 1)
    # print('END')
