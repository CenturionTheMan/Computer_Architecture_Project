import numpy as np


def tens_to_bin(num):
    res = [int(i) for i in list('{0:0b}'.format(num))]
    return res


def bin_to_tens(num):
    res = 0
    base = 0
    for bit in reversed(num):
        res = res + bit * np.power(2, base)
        base = base + 1
    return res


def calculate_s(X, p, r, k):
    s = 0
    vec_index = 0
    i = 1
    while i <= k:
        sub_X = None
        if i + r >= len(X):
            sub_X = X[0:len(X) - vec_index]
        else:
            sub_X = X[len(X) - vec_index - r:len(X) - vec_index]
        sub_x = bin_to_tens(sub_X)
        cons = int(np.power(2, r * (i - 1))) % p
        s = s + sub_x * cons
        i = i + 1
        vec_index = vec_index + r
    return s


def algorithm():
    X = tens_to_bin(262143)
    P = tens_to_bin(47)

    x = bin_to_tens(X)
    p = bin_to_tens(P)
    r = int(np.ceil(np.log2(p)))
    k = int(np.ceil(len(X) / r))
    print('x=', x, '| p=', p, '| r=', r, '| k=', k)
    s1 = calculate_s(X, p, r, k)
    print('S1=', s1, '| X%P=', x%p)


if __name__ == '__main__':
    algorithm()
