from NumbersManipulations import *
from ModuloAlgorithm import modulo_computation_algorithm as modulo


def calculate_modular_product(a: int, b: int, p: int):
    a_bin = tens_to_bin(a)
    b_bin = tens_to_bin(b)

    if len(a_bin) < len(b_bin):
        a_bin = extend_bin_with_zeros(a_bin, len(b_bin) - len(a_bin))
    elif len(b_bin) < len(a_bin):
        b_bin = extend_bin_with_zeros(b_bin, len(a_bin) - len(b_bin))

    bits_per_subvector = -1
    subvectors_amount = -1
    while bits_per_subvector < 0:
        if len(a_bin) % 4 == 0:
            bits_per_subvector = 4
            subvectors_amount = len(a_bin)/bits_per_subvector
        elif len(a_bin) % 3 == 0:
            bits_per_subvector = 3
            subvectors_amount = len(a_bin)/bits_per_subvector
        elif len(a_bin) % 2 == 0:
            bits_per_subvector = 2
            subvectors_amount = len(a_bin)/bits_per_subvector
        else:
            a_bin = extend_bin_with_zeros(a_bin, 1)
            b_bin = extend_bin_with_zeros(b_bin, 1)

    a_subvectors = split_bit_array_into_subvectors(a_bin, subvectors_amount)
    b_subvectors = split_bit_array_into_subvectors(b_bin, subvectors_amount)

    a_subvectors.reverse()
    b_subvectors.reverse()

    result = 0
    a_index = 0
    for a_sub in a_subvectors:
        a_index = a_index + 1
        b_index = 0
        for b_sub in b_subvectors:
            b_index = b_index + 1
            pow_to_raise = (a_index + b_index - 2) * bits_per_subvector
            cons = int(pow(2, pow_to_raise))
            s_tmp = bin_to_tens(a_sub) * bin_to_tens(b_sub) * cons
            s_tmp = s_tmp % p
            result = result + s_tmp
    result, iterations = modulo(result, p)
    return result
