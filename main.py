import numpy as np


def tens_to_bin(num):
    bits_arr = [int(i) for i in list('{0:0b}'.format(num))]
    return bits_arr


def bin_to_tens(bits_arr):
    res = 0
    base = 0
    for bit in reversed(bits_arr):
        res = res + bit * np.power(2, base)
        base = base + 1
    return res


def calculate_s(bits_arr, p, r, k):
    s = 0
    vec_index = 0
    i = 1
    while i <= k:
        sub_X = None
        if i + r >= len(bits_arr):
            sub_X = bits_arr[0:len(bits_arr) - vec_index]
        else:
            sub_X = bits_arr[len(bits_arr) - vec_index - r:len(bits_arr) - vec_index]
        sub_x = bin_to_tens(sub_X)
        cons = int(np.power(2, r * (i - 1))) % p
        s = s + sub_x * cons
        i = i + 1
        vec_index = vec_index + r
    return s


def algorithm(x, p):
    X = tens_to_bin(x)
    P = tens_to_bin(p)
    r = int(np.ceil(np.log2(p) - 1))
    k = int(np.ceil(len(X) / r))
    print('x=', x, '| p=', p, '| r=', r, '| k=', k)
    s1 = calculate_s(X, p, r, k)
    s_temp = s1
    while s_temp >= 2 * p:
        S_temp = tens_to_bin(s_temp)
        n_temp = len(S_temp)
        k_temp = int(np.ceil(n_temp/r))
        s_temp = calculate_s(bits_arr=S_temp, p=p, r=r, k=k_temp)
    result = 0
    if p <= s_temp:
        result = s_temp - p
    else:
        result = s_temp
    return result


if __name__ == '__main__':
    x = 262143
    p = 47
    x_mod_p = algorithm(x, p)
    print(f'{x}(mod{p}) = {x % p}')
    print('algorithm result =', x_mod_p)
