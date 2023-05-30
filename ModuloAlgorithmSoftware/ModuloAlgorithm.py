from NumbersManipulations import *


# Function to calculate 's' value
def calculate_s(bits_arr, p, r, k):
    s = 0
    i = 1
    for i in range(1, k + 1):
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
    s_temps = []

    if len(X) < k * r:
        X = extend_bin_with_zeros(X, k * r - len(X))

    X = split_bit_array_into_subvectors(X, k)
    s1 = calculate_s(X, p, r, k)

    s_temp = s1
    loop_counter = 1
    s_temps.append(s_temp)
    while s_temp >= 2 * p:
        loop_counter = loop_counter + 1
        S_temp = tens_to_bin(s_temp)
        n_temp = len(S_temp)
        k_temp = int(math.ceil(n_temp / r))
        if len(S_temp) < k_temp * r:
            S_temp = extend_bin_with_zeros(S_temp, k_temp * r - len(S_temp))
        S_temp = split_bit_array_into_subvectors(S_temp, k_temp)
        s_temp = calculate_s(bits_arr=S_temp, p=p, r=r, k=k_temp)
        # to do usuniecia:
        # print(f"s_temp: {s_temp}")
        # print(f"loop counter: {loop_counter}")
        # print(f"s_temps: {s_temps}")
        s_temps.append(s_temp)
    if p <= s_temp:
        return s_temp - p, loop_counter, s_temps
    else:
        return s_temp, loop_counter, s_temps
