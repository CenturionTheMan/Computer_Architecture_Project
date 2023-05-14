import random
import numpy as np


def tens_to_bin(num):
    bits_arr = [int(i) for i in list('{0:0b}'.format(num))]
    return bits_arr


def bin_to_tens(bits_arr):
    res = 0
    base = 0
    for bit in reversed(bits_arr):
        res = res + bit * pow(2, base)
        base = base + 1
    return res


def split_bit_array_into_subvectors(bits_array, subvectors_amount):
    result_array = np.array_split(bits_array, subvectors_amount)
    return result_array


def extend_bin_with_zeros(bits_arr, zeros_amount):
    zeros_to_add = []
    for i in range(zeros_amount):
        zeros_to_add.append(0)
    zeros_to_add.extend(bits_arr)
    return zeros_to_add


def calculate_s(bits_arr, p, r, k):
    s = 0
    i = 1
    for i in range(1,k+1):
        sub_X = bits_arr.pop()
        sub_x = bin_to_tens(sub_X)
        cons = int(np.power(2, r * (i - 1))) % p
        s = s + sub_x * cons
    return s


def modulo_computation_algorithm(x, p):
    X = tens_to_bin(x)
    r = int(np.ceil(np.log2(p)))
    k = int(np.ceil(len(X) / r))

    if len(X) < k * r:
        X = extend_bin_with_zeros(X, k * r - len(X))

    X = split_bit_array_into_subvectors(X, k)
    s1 = calculate_s(X, p, r, k)

    s_temp = s1
    while s_temp >= 2 * p:
        S_temp = tens_to_bin(s_temp)
        n_temp = len(S_temp)
        k_temp = int(np.ceil(n_temp/r))
        if len(S_temp) < k_temp * r:
            S_temp = extend_bin_with_zeros(S_temp, k_temp * r - len(S_temp))
        S_temp = split_bit_array_into_subvectors(S_temp, k_temp)
        s_temp = calculate_s(bits_arr=S_temp, p=p, r=r, k=k_temp)

    if p <= s_temp:
        return s_temp - p
    else:
        return s_temp


if __name__ == '__main__':
    maxX = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    maxP = [1,1,1,1,1,1,1,1]
    x = bin_to_tens(maxX)
    p = bin_to_tens(maxP)
    x_mod_p = modulo_computation_algorithm(x, p)
    print(f'{x}(mod{p}) = {x % p}')
    print('algorithm result =', x_mod_p)
