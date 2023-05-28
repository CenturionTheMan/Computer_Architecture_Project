import math
import numpy as np


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
