from main import *

X = 6000
P = 21
res = modulo_computation_algorithm(X, P)[0]
print(f'algorithm = {res} | exact = {X % P}')